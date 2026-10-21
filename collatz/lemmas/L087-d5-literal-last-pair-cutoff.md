# L087 — d=5 literal last-pair cutoff

## Hypotheses

Take L055's 25 indexed pairs, changing only H_0=35 and
H_24=32670626. Every J is unchanged. Set B=9250245 and
kappa=23/11. For an integer 2<=t<=B put
b_0=...=b_22=0, b_23=t, b_24=B-t and a_i=2+18b_i.
Suppose real s_0,...,s_25 satisfy s_25=s_0, s_i>=540/11 and,
in literal indexed order, for every 0<=i<25,

\[
s_{i+1}=2^{-a_i}\left((27/16)^{J_i}(3/2)^{H_i}s_i
                  -(12/11)(3/2)^{H_i}-1\right)+\kappa,
\qquad 4J_i\log2\le\log s_i+\log(11/4).
\]

Every outgoing own-input guard and endpoint, including closure, is
required. There is no minimum, H guard, seed, integer-junction, parity,
residue, exact-valuation, primitive-count or actual-word premise.

## Conclusion

No such tuple exists for any integer 2<=t<=9250245. More precisely,
L077 gives the row24 right-minus-left J margin at t=2 the strict upper
bound F^C(5)<0 displayed below, and rejects every
larger admitted t as well, including t=B where a_24=2.

This is RESEARCH/KNOWN_IMPORTED under the prior IMPORT assessment
`drafts/literature/2026-10-19-d5-literal-last-pair-cutoff.md`.
It is a local applicability result using already audited certificates,
not a new cutoff mechanism or progress beyond those inputs. The separate
critical applicability audit below found no defect. No t=0,1 feasibility or exclusion, early-support
assembly, cyclic-order reduction, integer exclusion or actual-word
application is asserted. Universal eventual descent remains unresolved.

## Proof

Apply the independent sufficient criterion L077, not the full C077a
conjunction. Here r=25, p=23, q=24 and tau=2<=B. The unchanged
L055 J table is strictly increasing with J_0=8; H_0=35, H_24=32670626
and all unchanged H_i are at least 3. The pairs are exactly the d=5
member of L084. The allocation, literal order, endpoint, lower-domain
and non-strict own-input J hypotheses above are exactly L077 (6).

Use the following L084 independent C constants:

\[
\lambda_-=10584/10^{14},\quad\lambda_+=10585/10^{14},\quad e=2,
\quad T=24,\quad U=20000000000,
\]
\[
\ell=693147180559/10^{12},\quad
u=1098612288669/10^{12},\quad v=1011600911679/10^{12},
\]
\[
w_5=10^8(2/3)^4,\quad L_0=1,\quad
L_i=w_5 2^{i-1}\ (1\le i\le24),\quad
Q=\frac{23}{11}\sum_{i=0}^{24}\frac1{L_i}.
\]

Here are the exact matches to every required data test; their proofs
and complete audited finite evidence are imported from L084.

* L077 (3): L084 (2) certifies the positive Lambda enclosure for
  K=397573379,N=630138897. L084's independent cutoff section proves
  eta_24>=eta_0>2 and
  e(1-lambda_+)/lambda_+=39999999995766/2117>47.
* L077 (4), incoming bounds: L084 (1), (5) and its independent C/H
  audit certify 0<L_i<=C_i(2) for every incoming index 0 through 24.
  Q is its complete finite reciprocal sum, with equality in the required
  Q bound. At this boundary the actual two final tails are
  a_23=38 and a_24=166504376, exactly the audited C package.
* L077 (4), cap and analytic bounds: L084 (6) and the completed audit
  certify Q/lambda_-+Q+kappa/L_24<=U<exp(24) at d=5. Its complete
  failure list places C-cap failures only at d=34,...,37 and explicitly
  records that all other cap comparisons pass. Thus this application
  uses the independently audited d=5 cap, not the displayed (7) bound
  whose stated range is only d=1,...,4. L084 (2) supplies all three
  logarithm directions and ell>0.
* L077 (5): L084 (8) gives precisely
  \[
  F^C(5)=-2102267684691/500000000000-4(u-\ell)<-4.20<0.
  \]
  Its audited incoming exponents are
  k_24=271907920-4 and d_24(2)=306970783-4; J_24=30998279.
  This is the required expression
  T+k_24 u-(d_24(2)+4J_24)ell+v, with the extra 36 boundary
  halvings retained in d_24(2).

All L077 (3)–(5) hypotheses therefore hold independently. Invoke its
full-interval conclusion: row24's own-input non-strict J guard fails
for every integer tau<=t<=B. This contradicts the corresponding
hypothesis above. The final tail at t=B is 2 and is included in that
conclusion; no sampling or additional monotonicity proof is used here.

L084's failed d=5 row0 S offset is not an L077 premise. Neither
C077a's unavailable full reduction nor L086's early-support result is
invoked. Attempt 032's full-test stop and both original d=0 rational
witnesses remain valid. This proof adds no certificate calculation or
survivor inference.

The standard upstream affine input, already specialized and audited in
L077/L084, is Halbeisen–Hungerbuehler, *Optimal bounds for the length
of rational Collatz cycles*, Acta Arith. 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Only formal real affine composition with positive fixed-point denominator
is used. The positive-real analytic inputs are the already inspected
[DLMF 4.5.1](https://dlmf.nist.gov/4.5.E1),
[4.6.4](https://dlmf.nist.gov/4.6.E4) and
[4.2.19](https://dlmf.nist.gov/4.2.E19); exact outward bounds are
imported from L084. No source theorem or criterion is reproved.

### Independent critical applicability audit — 2026-10-20, step 353

This RESEARCH/REPRODUCTION proof audit uses the prior SPECIALIZE
assessment `drafts/literature/2026-10-19-d5-literal-last-pair-critical-audit.md`.
It found no defect in this citation-only application. This validates the
existing restricted input, not a new criterion, numerical certificate,
table exclusion beyond L087, or advance beyond the cited machinery.
The precise primary citations above and their ready assessments are
reused; no source reproof or duplicate certificate reconstruction is needed.

**Table and subsystem.** The complete L055 table has strictly increasing
integer J values from 8 through 30998279. Replacing its H_0=40 by 35
and H_24=32670621 by 32670626 gives exactly L084's d=5 member;
all H values remain at least 3. The opposite changes preserve sum H,
and the last-pair allocation preserves sum a=2*25+18B. Consequently
L077 (1) uses exactly K=397573379 and N=630138897 from L084 (2).
Here r=25,p=23,q=24,B=9250245,tau=2, with tau<=B. Each real
input, lower-domain bound, own-input non-strict J guard and shifted
endpoint is literally L077 (6), including s_25=s_0. There is no
rotation, minimum selection or appeal to the full L055 witness system.

**All of L077 (3).** L084 (2) gives the strict positive Lambda enclosure
inside the required weak endpoints, with lambda_+<1. Its independent
C section and all-member audit prove eta_0>2 and eta_24>=eta_0 for
every tested member, including this one. Thus e=2 satisfies both eta
requirements. The same audited exact value
e(1-lambda_+)/lambda_+=39999999995766/2117>47 meets the domain
test. None of these facts depends on a successful S offset test.

**Every incoming bound and the complete sum in L077 (4).** At tau=2,
row23 has tail 38 and row24 has tail 166504376. The former contributes
to C_24; the latter contributes to the closing product C_25, hence to
Lambda and the fixed-point denominator. L084 (5) and its all-member
audit prove c_0>w_5 and c_i>2 for 1<=i<=23 with these actual tails.
Their induction supplies exactly L_0=C_0=1 and 0<L_i<=C_i(2)
for all 1<=i<=24. No incoming index is omitted, and C_25<1 is not
required to satisfy a prefix lower bound. The complete reciprocal sum
is 1+(2/w_5)(1-2^(-24)); multiplying by kappa gives precisely the
Q displayed above. Thus the required Q comparison holds with equality,
without an infinite-sum replacement or loss of the i=24 contribution.

**The d=5 normalized cap and analytic signs.** The required expression
is L084 (6)'s R_C(5)=Q/lambda_-+Q+kappa/L_24, not R_H(5) with
its different final denominator. Display (7) alone covers only d<=4
and would not justify this application. The canonical completed audit
explicitly reconstructs both caps for all 37 members, records cap
failures only for d=34,...,37, and states that every other cap comparison
passes. This is affirmative coverage of R_C(5)<=20000000000.
The same audit checks the degree-40 positive exponential lower sum at
24 and the intervening thresholds, giving U<exp(24). The constants
ell,u,v match L084 (2), with ell>0, ell<log2, log3<u and
log(11/4)<v. These are certified outward bounds, not rounded estimates.
No conflict between the displayed narrower bound and the all-member
audit was found; relying on that completed audit does not require
repeating its 37-table arithmetic in this applicability check.

**L077 (5), own-input contradiction and the entire interval.** L084 (8)
and its audit give k_24=271907920-4=271907916 and
d_24(2)=306970783-4=306970779. The incoming denominator includes
the extra 36 halvings at row23; the changed closing tail is retained
in N, not incorrectly inserted in this incoming exponent. With the
unchanged outgoing J_24=30998279, T=24 and the same ell,u,v, the
expression T+k_24*u-(d_24(2)+4J_24)*ell+v is exactly the cited
F^C(5)=-2102267684691/500000000000-4(u-ell)<-4.20<0.
The positive coefficient of log3 requires its upper enclosure, and the
negative coefficient of log2 requires its lower enclosure; both match.

L077's proved conclusion now applies to every real tuple satisfying
the endpoints: its positive-denominator uniqueness identifies the tuple
to which the boundary estimate applies, and its full-interval result
makes row24's right-minus-left J margin strictly negative for every
integer 2<=t<=B. The assumed non-strict guard requires this same margin
to be nonnegative. This is a strict contradiction at the correct input
s_24. At t=B, row24 has tail 2; L077 explicitly includes that boundary
and does not assume growth of either varying row. Neither sampling nor
a new monotonicity assertion is substituted for its quantified result.

**Scope and preserved failures.** L084's d=5 failed row0 S offset is
not a premise of L077 (3)–(5). Attempt 032 stops the full sufficient-test
conjunction and remains valid. No use of C077a's full conclusion or
L086's early-support result occurs here. Neither survivor t=0,1 receives
a feasibility, H-guard or integrality verdict. Both original d=0 rational
witnesses have different tables and remain unaffected. No minimum,
H/seed, integer-junction, parity, valuation, primitive-count, actual-word
or realization-converse assumption has entered the proof.

The direct mathematical inputs remain L055, L077 and L084. The proof
and dependency structure have not changed, so PROOF.md and DAG.md are
unchanged; this canonical audit supersedes their pending-audit wording
for L087. Order reduction, survivor exclusion, actual-word transfer and
universal eventual descent remain unresolved. Full matching Mathlib
coverage remains unchecked.

## Mathlib

Full matching Mathlib coverage has not been checked. Supporting affine,
logarithm and exponential facts do not constitute this table application;
no absence or formal verification is claimed.
