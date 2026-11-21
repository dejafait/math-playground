# Lemma 945: a uniform bound for the actual theta kernel

## Hypotheses

Let u>=0 and let K be exactly the unnormalized kernel of L019:

    K(u)=sum_(n>=1) [8 pi^2 n^4 exp(9u/2)-12 pi n^2 exp(5u/2)]
                         exp(-pi n^2 exp(2u)).

Import George Csordas, *Fourier transforms of positive definite kernels
and the Riemann xi-function*, [arXiv:1309.0055v2](https://arxiv.org/pdf/1309.0055v2),
21 February 2014, printed p10, equation (4.2) and Theorem 4.1(i),(ii),(v).
For that equation's Phi these assert positivity for t>=0, analyticity
in |Im t|<pi/8, and Phi'(t)<0 for t>0. The cited theorem is used as
stated; this is not an independent audit of its originating proof.
Reuse only L826(8)'s independently audited subclaim 1<K(0)<2,
with the integer-program trust and qualifications recorded there.

## Conclusion

For every u>=0,

    0<K(u)<=K(0)<2.

In particular 0<K(u)<=2 on the entire positive half-line including
zero. This is a known-result specialization, not a new theta maximum
theorem. It neither establishes any density crossing nor any Xi mixed
positivity, parameter endpoint sign or RH conclusion.

## Proof

Source equation (4.2) defines

    Phi(t)=sum_(n>=1) pi n^2 (2 pi n^2 exp(4t)-3)
                              exp(5t-pi n^2 exp(4t)).

The coordinate identification in L605 is exact: substitute t=u/2
and multiply each summand by 4. The first coefficient becomes
8 pi^2 n^4 exp(9u/2), the second -12 pi n^2 exp(5u/2),
and the remaining exponential is exp(-pi n^2 exp(2u)). Both series
converge, including at zero, giving K(u)=4 Phi(u/2). No probability
normalization, transform value or Stein ratio enters this identity.

L019 gives K(u)>0. For u>0, source analyticity makes Phi continuous
on [0,u/2] and differentiable on its interior. The mean value theorem
and Theorem 4.1(v) therefore give Phi(u/2)<Phi(0). Multiplying by
the positive factor 4 gives K(u)<K(0). For u=0 the comparison with
K(0) is equality; no strict derivative inequality at zero is needed.

Finally L826(6)-(8), specifically r=0, gives 1<K(0)<2. Its complete
n=1,...,8 finite sum and n>=9 tail are included. The independent
step636 audit recorded in L826 verifies containment of the full
derivative interval and the strict rational comparisons in (8).
This application reuses that audited endpoint input; it does not
require L826's Q_3 endpoint claims or assume global total positivity.
The certificates are `scripts/log-theta/endpoints_634.json` and
`scripts/log-theta/endpoints_audit_636.json`. They were not replayed
in this step. Ordinary trust in their documented integer/rational
program execution remains, rather than formal verification.
Combining the comparisons proves the conclusion.

The relevance is to a smaller common factor bound in L944's twelve
factor error estimates. No replacement error allowance or sign cover
is derived here; those require their own checked propagation.

## Mathlib

Not checked: a matching full theorem, the cited Phi decrease result,
and a formal endpoint enclosure were not located or asserted absent.
General mean value theorems would support the final comparison but
do not supply either essential theta input. Coverage remains unknown.
