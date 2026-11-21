# Balanced-saddle attempt — step52 working record

Approved target: the exact TARGET in
`drafts/literature/2026-11-09-l938-balanced-tail-attempt-51.md` (EXPLORE
before invocation). Main gap: L030–L032/C032a actual-Xi all-degree mixed
positivity. Seek one eventual sign of L938's fixed density, for possible
use in a later full variation argument; no finite-energy or parameter
endpoint sign is assumed.

Inputs read: L019's full kernel, L058's domination, L938 equations
(3)–(10) and all 34 rows; the prior source comparison and fixed-cell
stop/audit. No cross-notebook input. Retain M_0^12, all twelve factors
and factorials, without multinomial multiplicities.

First discriminator: form the full signed polynomial in the simplex
variables, factoring out the common product of t_i^(-1/2). At
t_i=1/12 its value is 12^(-12) times
sum_alpha c_alpha / product_k ((2k)!)^(alpha_k). Evaluate exactly,
independently against the Newton recurrence. No value or sign asserted
yet. Cancellation ends the attempt; no higher-order fallback.

If nonzero, use r=sqrt(E/12). The full-kernel phase and every simplex
boundary require localization and a relative remainder. Katsevich
arXiv:2406.12706v3 Thm2.12/Remark2.5 is the assessed method; BKR is
parked and is not an input. A positive saddle coefficient by itself
does not prove a tail sign. Stop at the first unpaid localization or
remainder estimate and preserve the precise obligation.

Unresolved regardless of this attempt: global finite-energy variation,
det H2 parameter endpoints, contacts, other degrees, initialization,
realization and global continuation. No complete RH candidate.

## Saved development before final write-up

The exact script `scripts/heat/l938-balanced-coefficient-52.py` gives
C=1/371319795000>0 from all 34 rows and independently from the six
Newton coefficients; absolute/signed sum is 3893731/1024. The JSON
certificate is adjacent. This is algebra only, not a tail certificate.

Set x_i=r^2+r y_i, sum y_i=0, y_i>-r, r=sqrt(E/12), n=pi exp(2r).
Write w_i=1+y_i/r, u_i=r sqrt(w_i),
z_r=sum_i (exp(2(u_i-r))-1-y_i).
The prospective exact prefactor is
2^(-12)(8pi^2)^12 r^23 exp(54r-12n), and the remaining amplitude is
the full 34-term factorial-weighted polynomial in w, times
product w_i^(-1/2), exp((9/2)sum(u_i-r)), and product q(u_i), where
q=K/(8pi^2 exp(9u/2-pi exp(2u))).

Key localization argument to verify in the canonical proof: for r>=2,
h_r(y)=exp(2r(sqrt(1+y/r)-1))-1-y is nonnegative on [-r,infinity).
For y<=-1 use h>=-1-y; for -1<=y<=0 use convexity; for y>=0 the
second derivative is >=3/4, hence h>=3y^2/8. The sum constraint then
gives z_r>=sum_i y_i^2/32. Thus no boundary minimum competes with
the balanced point. H_r=(1-1/(2r))(I+11x11 all-ones matrix).

With Katsevich R=r, d=11, the local ball shrinks like r exp(-r),
so derivatives through phase order four/amplitude order two should
stay bounded. Outside it, the global amplitude L1 bound is O(r^11):
concavity gives sum u_i<=12r, q is globally bounded, and the full
product w_i^(-1/2) has a finite Dirichlet integral. The proposed
normalized outer bound is O(r^11 exp(11r-11r^2/32)), tending to zero.
The remaining work is to write and check these estimates, the full
theta derivative bounds, and the exact application of Thm2.12 with
Remark2.5. No final tail theorem is asserted in this working record.

## Completion pointer

The estimates above were completed in canonical L939, including the
full-theta derivative majorant, all boundary faces and the relative
remainder. That lemma is newly written and unaudited. This file
preserves the earlier reasoning stages and is not a second proof.
