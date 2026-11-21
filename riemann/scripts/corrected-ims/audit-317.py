"""Instrument the unchanged fixed-witness certificate; preserve every old output.

Run from the active notebook with python3 scripts/corrected-ims/audit-317.py.
This checks implementation domains and enumerates prime powers independently;
the analytic justification is canonical in L750's step317 audit.
"""
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent
source = (ROOT / "certificate-315.cpp").read_text()


def replace_once(old, new):
    global source
    assert source.count(old) == 1, old
    source = source.replace(old, new)


replace_once("#include <algorithm>", "#include <algorithm>\n#include <cfenv>")
replace_once(
    "struct I { double l,h; I(double x=0):l(x),h(x){} I(double a,double b):l(a),h(b){} };",
    """struct I { double l,h;
 I(double x=0):l(x),h(x){if(!isfinite(x))throw runtime_error("nonfinite point");}
 I(double a,double b):l(a),h(b){if(!isfinite(a)||!isfinite(b)||a>b)throw runtime_error("invalid interval");}
};
double max_trig=0,max_atan=0,max_exp_base=0,max_delay_width=0;
double min_log_base=2,max_log_base=1,min_delay_cell_margin=1;
int simpson_calls=0,delay_calls=0;""",
)
replace_once(
    "I v(z),sum(1),term(1);",
    'max_exp_base=max(max_exp_base,abs(z)); if(abs(z)>.125)throw runtime_error("exp base"); I v(z),sum(1),term(1);',
)
replace_once(
    "I logUnit(I x){I t=",
    'I logUnit(I x){if(x.l<1||x.h>2)throw runtime_error("log base"); min_log_base=min(min_log_base,x.l);max_log_base=max(max_log_base,x.h);I t=',
)
replace_once(
    "I atanSmall(I x){I t=",
    'I atanSmall(I x){max_atan=max(max_atan,max(abs(x.l),abs(x.h)));if(max_atan>.25)throw runtime_error("atan domain");I t=',
)
for function in ("sinSmall", "cosSmall"):
    replace_once(
        f"I {function}(I x){{I term",
        f'I {function}(I x){{max_trig=max(max_trig,max(abs(x.l),abs(x.h)));if(max_trig>4)throw runtime_error("trig domain");I term',
    )
replace_once(
    "I u=I(1)/I(a);if(u.l<k)",
    'if(a<=0||k<2||k>4)throw runtime_error("eta endpoint bound domain"); I u=I(1)/I(a);if(u.l<k)',
)
replace_once(
    "I derivative4){I h=",
    'I derivative4){if(n<=0||n%2||a.h>=b.l||derivative4.l<0)throw runtime_error("Simpson hypotheses");simpson_calls++;I h=',
)
replace_once(
    "int m=(int)floor((u.l+u.h)/2);I corr(0);",
    '''int m=(int)floor((u.l+u.h)/2);
 if(floor(u.l)!=m||floor(u.h)!=m)throw runtime_error("delay crosses interpolation cell");
 delay_calls++;max_delay_width=max(max_delay_width,up(u.h-u.l));
 min_delay_cell_margin=min(min_delay_cell_margin,min(dn(u.l-m),dn(m+1-u.h)));
 I corr(0);''',
)
replace_once(
    "cout<<setprecision(17);if(numeric_limits<double>::is_iec559!=true)",
    '''if(fegetround()!=FE_TONEAREST||numeric_limits<double>::digits!=53||numeric_limits<double>::radix!=2)throw runtime_error("binary64 environment");
 volatile double tiny=numeric_limits<double>::denorm_min(),one=1;
 if(!(tiny*one>0))throw runtime_error("subnormals flushed");
 cout<<setprecision(17);if(numeric_limits<double>::is_iec559!=true)''',
)
replace_once(
    'cerr<<"Defect ["<<defect.l',
    '''ofstream audit("scripts/corrected-ims/implementation-domains-317.json");audit<<setprecision(17);
 audit<<"{\\"status\\":\\"PASS\\",\\"max_trig_abs\\":"<<max_trig<<",\\"trig_required\\":4,\\"max_atan_abs\\":"<<max_atan<<",\\"atan_required\\":0.25,\\"max_exp_base_abs\\":"<<max_exp_base<<",\\"exp_required\\":0.125,\\"log_base_range\\":["<<min_log_base<<","<<max_log_base<<"],\\"log_required\\":[1,2],\\"max_delay_interval_width\\":"<<max_delay_width<<",\\"min_delay_cell_margin\\":"<<min_delay_cell_margin<<",\\"required_cell_margin\\":0,\\"simpson_calls\\":"<<simpson_calls<<",\\"all_simpson_subinterval_counts_even\\":true,\\"delay_calls\\":"<<delay_calls<<",\\"prime_powers\\":[";
 for(size_t j=0;j<pp.size();j++){if(j)audit<<",";audit<<pp[j].first;}audit<<"],\\"failures\\":[]}\\n";
 cerr<<"Defect ["<<defect.l''',
)
instrumented = ROOT / "instrumented-317.cpp"
instrumented.write_text(source)
binary = "/private/tmp/riemann-ims-instrumented-317"
subprocess.run(["clang++", "-O2", "-std=c++17", "-ffp-contract=off",
                str(instrumented), "-o", binary], check=True)
with (ROOT / "certificate-instrumented-317.json").open("w") as out:
    subprocess.run([binary], stdout=out, check=True)


def prime_power(n):
    # Independent integer trial factorization, rather than a prime-list sieve.
    p = next((d for d in range(2, int(n**0.5) + 1) if n % d == 0), n)
    m = n
    while m % p == 0:
        m //= p
    return m == 1


domains = json.loads((ROOT / "implementation-domains-317.json").read_text())
original = json.loads((ROOT / "certificate-315.json").read_text())
replayed = json.loads((ROOT / "certificate-replay-317.json").read_text())
instrumented_result = json.loads((ROOT / "certificate-instrumented-317.json").read_text())
constants = json.loads((ROOT / "constants-replay-317.json").read_text())
expected = [n for n in range(2, 6561) if prime_power(n)]
actual = domains["prime_powers"]
checks = {
    "unmodified_replay_identical": original == replayed,
    "instrumentation_result_identical": original == instrumented_result,
    "constants_replay_identical": constants == json.loads((ROOT / "constants-315.json").read_text()),
    "all_fourteen_constants_pass": len(constants["checks"]) == 14 and all(c["pass"] for c in constants["checks"]),
    "all_prime_powers_exactly_once": sorted(actual) == expected,
    "all_local_prime_powers_exactly_once": sorted(n for n in actual if n < 729) == [n for n in expected if n < 729],
    "all_delay_calls_accounted": domains["delay_calls"] == len(expected) + sum(n < 729 for n in expected),
    "all_five_moments_simpson_checked": domains["simpson_calls"] == 5,
    "strict_negative_defect": instrumented_result["Delta"][1] < 0,
    "global_and_local_energies_positive": min(instrumented_result[k]["smooth_energy"][0] for k in ("f", "v1")) > 0,
}
summary = {
    "status": "PASS" if all(checks.values()) else "FAIL",
    "checks": checks, "prime_power_count": len(expected),
    "local_prime_power_count": sum(n < 729 for n in expected),
    "Delta": instrumented_result["Delta"], "required_upper": 0,
    "failures": [name for name, value in checks.items() if not value],
    "scope": "Fixed L750 witness only; analytic proof audited separately in L750.",
}
path = ROOT / "audit-summary-317.json"
path.write_text(json.dumps(summary, indent=2) + "\n")
print(f"{summary['status']}: Delta {summary['Delta']}; required upper < 0")
print(f"Prime powers global/local: {len(expected)}/{summary['local_prime_power_count']}; failures: {summary['failures']}")
print(f"Full evidence: {path.relative_to(Path.cwd())}; {ROOT.relative_to(Path.cwd())}/implementation-domains-317.json")
raise SystemExit(0 if all(checks.values()) else 1)
