# One bounded mixed affine supported-unit attempt

STEP_ID: beal-2026-10-16-252-separated-eleven-affine-attempt

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-16-separated-eleven-supported-unit.md`.
This is RESEARCH, classified REPRODUCTION. The exact approved target is:
Construct a supported norm-square unit in V_S whose valuation parities at the two rational eleven-adic degree-one factors are unequal.

## Saved before calculation

The main gap is primitive integer emptiness. The intermediate target is
one actual separating supported unit in L074/L076's V_S. Such a unit
could add a restriction beyond L077's rational-cubic family. Further
pruning to eleven, the localized class contribution, useful rank and
integer lifting would remain unresolved.

Use precisely L069's m(k)=0 and L077's f(t)=t^3-t^2+t+1=0 in D,
with theta=8-14t+6t^2. Fix L041's base places in order k=8,2 mod 11;
the degree-one factor above each has t=6 mod 11. The distinct
ramified quadratic factors have t=3 mod 11, by L073/L077.
Essential inputs: L033, L041, L069, L073, L074, L076, L077.
No cross-notebook input or class-number assumption is made.

The FINITE family is z=a+b*k+c*t with -32<=a<=32, 1<=b<=4,
c in {-4,-3,-2,-1,1,2,3,4}, and gcd(a,b,c)=1. The raw cap is
65*4*8=2080 triples, with no adaptive enlargement. These elements mix
the two specified fields; the complete rational-cubic family is not
searched again. First compute the exact relative norm n=N_D/K(z),
then N_K/Q(n). Record every candidate and its norm, strip only 2 and
11, and reject any residual factor >1. For any survivor, certify the
supported inverse, form u=z/n, and check N_D/K(u)=n^(-2) exactly.
Then certify the two ordered maximal-prime valuation parities of u;
do not assume norm correction preserves the old parities. The
candidate-family cap includes all calculations in this step.

Use exact determinant arithmetic with complete replay; no floating
norm, uncertified maximal order, or class/unit backend is needed.
Support can be certified by integral multiplication matrices with
determinant a signed product of 2 and 11; their adjugates provide
inverses over Z[1/22]. A failed support test rejects this proposed
element, not every possible product of rejected elements.

Continuation test: a fully certified separating unit meets the target;
a proved universal equality obstruction stops it; exhaustion of this
finite family decides neither. Save all arithmetic and any failure.
Do not extend this family after failure. ATTEMPTS/032-033 and all
existing unfinished work remain preserved.

## Result

The cap was exhausted without a supported element: 2080 raw triples,
306 excluded by the declared gcd condition, 1774 tested, zero supported
norms. The two exact tower computations agreed on every candidate;
all five consistency checks passed. The complete evidence is
`scripts/separated-eleven-unit/affine-certificate.json`, reproduced by
`python3 scripts/separated-eleven-unit/check_affine.py`.

For reproducibility, with d=a+bk the first computation uses

    n=N_D/K(d+ct)=d^3+c*d^2+c^2*d-c^3.

Indeed f has elementary symmetric functions 1,1,-1. Its four
coefficients as a polynomial in k are saved in every row. The norm
N_K/Q(n) is the determinant of multiplication by n on the complete
basis 1,k,...,k^11, reduced by the fixed monic m. The second tower
uses the complete degree-twelve extension D/F and the identity

    N_D/F(a+bk+ct)=b^12*m(-(a+ct)/b).

The homogenized Horner recurrence computes this element integrally in
1,t,t^2; its multiplication determinant gives N_F/Q, independently
matching the first absolute norm in all 1774 cases. D/F has degree
twelve because L069 and L077 identify the same degree-36 field D and
degree-three subfield F. Norm transitivity and the determinant/ideal
norm interface are the previously assessed Milne ANT v3.08,
Proposition 4.1 and norm definition, pp.68-69; no new general result is
claimed. Bareiss elimination performs only exact divisions, checked
at every step. The complete candidate loop, uniqueness, nonzero norms
and reconstruction of every stripped factor are checked, not sampled.

Each z is integral. An integral S-unit must have absolute norm a signed
product of 2 and 11: at every other rational prime the principal-ideal
norm formula sums zero valuations with positive residue degrees. Every
record instead has a residual integer factor strictly greater than one
after completely stripping 2 and 11. Its prime factorization is not
needed for this rejection. Thus none reaches the supported-inverse or
norm-correction stage of the declared strategy. We do not infer that a
ratio or a product of rejected elements fails: their outside prime
ideals might cancel. No full S-unit generation or global equality of
parities is established.

The certificate also records 322 candidates with different residue
vanishing flags a+b*k+3*c=0 mod 11 at k=8 and k=2. These are only
prospective local flags; no supported unit survived and no ordered
maximal-prime parity certificate was completed. They are not counted
as witnesses or new restrictions. Required witnesses: one; certified:
zero. L077's filtered unit bound stays fourteen versus required eleven.

Outcome: EXPLORATION, the first of three mathematical exploration
attempts in this cycle. This finite failure supplies no universal
nonexistence result and no beyond-source mathematical advance. The
full Beal target and all independent gaps remain open. No lemma,
PROOF.md change or DAG edge is warranted. Mathlib coverage is not
checked. All prior failures and artifacts are preserved.
