# Regularized Li/theta representation — working record, step165

Approved target: the exact Q_eta representation in the saved step163
assessment (SPECIALIZE, already present at invocation). Main gap remains
actual-Xi all-degree mixed positivity. No actual Li or mixed sign is assumed.

Inputs read: L019-L021, L024-L026, L030, L242, audited L964.
The assessment supplies the DLMF product/integral/chain-rule comparison;
no additional literature is needed for this bounded specialization.
The exact-Q_eta search found L964 and the current review, no second local
representation. Recorded generic-logarithm and theta-realization failures
remain constraints, not global bans on rational differentiation.

Partial derivation (not yet an audited result): set b=1/4, h=1/eta,
t=1/beta, and B_n(t)=t^(n-1)P_n(1/t)^2. This is a polynomial of degree
n-1, since 2 floor((n-1)/2)<=n-1. The summand becomes

    h B_n(t)/((t+h)(t+b)^n).

It is O(t^-2). Partial fractions at -h and -b appear to have coefficients
-d_1 and (-1)^(k-1)d_k, with all d_k>0. Thus, with F(x)=Xi(i sqrt x),
the candidate identity is

    Q_eta = sum_{k=1}^n d_k/(k-1)! * (log F)^(k)(b) - d_1 F'(h)/F(h).

The product gives absolutely convergent resolvents, rather than divergent
constant sums. Finite log differentiation expands each term into products
of positive integrals I_r(x)=int K(u) d_x^r cosh(sqrt(x)u) du. Partition
by the number of factors: odd blocks positive, even blocks negative;
the additional h-resolvent is retained with negative sign. This would
produce explicit N_n-R_n, not max(Q,0)-max(-Q,0).

Remaining checks: finite formula and signs of every d_k; n=1; all
multiplicities; compact uniform product differentiation; absolute theta
differentiation and Fubini; a finite inequality in actual theta moments
as the precise unpaid remainder condition. No claim that R_n<=N_n is
made, and no positive Stieltjes measure is used. Full proof and any
verification belong in a canonical lemma if this ansatz survives.

Completion: the ansatz survived. The full all-n argument, coefficient
recipe, absolutely convergent integrals and exact unpaid inequality
are now canonical in L966. The proof uses only the actual kernel and
paired nodes. Exact rational checks of the denominator-cleared identity
and the residue at -h passed for n=1,...,12; their full certificate is
scripts/li-theta/regularized-resolvent-check-165.json. These are finite
diagnostics, not the all-n proof or a theta-sign certificate. L966 remains
unaudited. R_n<=N_n is not established; positivity of this prescribed
eta family is not asserted sufficient for all mixed signs or RH.
