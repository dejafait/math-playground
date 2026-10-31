# Vertical-side norm test: working checkpoint

Approved target and source scope: `literature/2026-10-30-vertical-side-finite-measure-norm-test.md` (EXPLORE, saved before invocation). Main gap remains actual-Xi all-degree positivity. Test exactly the full-space M norm of L504's Q_a plus a finite nonnegative paired-side measure on [b,B]. L505/L507 are scope contrasts only. No source refresh, cross-notebook input, optimizer or duality premise is used.

Prospective downstream use: an O_R(a) norm would imply a one-sided Q bound on H_a after checking the side sign and endpoints. Discriminating test: prove that bound or a lower bound divergent relative to a for every allowed measure. A single failed measure would not decide the family.

## Partial construction saved before detailed estimates

Use two separated positive angular-frequency packets, each within a region where cos(sa)>0. Normalize each frequency by cos(sa)cosh(sb). Its paired side trace is then an average of cosh(sy)/cosh(sb), exactly, with no approximation through the tall interval [b,B]. The derivative in s of the logarithm of this ratio is y tanh(sy)-b tanh(sb), positive for y>b and negative for 0<=y<b. The high packet minus the low packet therefore has nonnegative side trace and a positive Q contribution. This is a proposed common witness independent of the measure; quantitative gap and real-axis norm estimates remain to be completed.

Choose centers on sa in 2pi Z at two fixed separated frequencies within (0,2pi R), and packet width O(1/a). A fixed smooth bump divided by cos(t)cosh(s_j b+t/4) should have two derivatives bounded by C exp(-s_j b); two integrations by parts would then give N<=C a exp(-s_low b). Need a positive uniform lower bound for Q, a common onset for every real T including center jumps, exact Fourier support/evenness/reality, finite functional norm, and the H_a distinction. No conclusion is yet recorded.

## Completed bounded test

The construction succeeds with centers s_1=2pi floor(Ra/4)/a and s_2=2pi floor(Ra/2)/a and a fixed smooth probability bump on (-1/4,1/4). The full proof and constants are canonical in L508. Exact normalized cosh ratios give the side sign for every y>=b; no error is integrated against unrestricted measure mass. The gap contribution is bounded below on b-y in [1/(pi R),2/(pi R)]. Two integrations by parts give M<=N<=C a exp(-s_1 b). Hence every allowed measure has norm at least c_R L^(R/8)/a, with ratio to a divergent at every sufficiently large real T.

This is an informative NEGATIVE for the entire approved side-measure family, not a counterexample on H_a or a resolution of RH. The witness vanishes at the side endpoints at height b, so it is outside H_a. L508 awaits an independent audit; its new audit-coverage nomination is REVIEW_REQUIRED. Existing horizontal and exterior-majorant stops are preserved. No mathematical script or numerical evidence is needed for this elementary proof.
