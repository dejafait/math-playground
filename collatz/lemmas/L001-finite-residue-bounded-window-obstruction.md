# L001 — Obstruction to bounded-window descent with a finite residue correction

## Hypotheses

Let T on positive integers be n/2 for even n and (3n+1)/2 for odd n. Let q,K be positive integers, let N be a positive integer, and let h:{0,...,q-1}->R be any function. Put

\[
V(n)=\log n+h(n\bmod q).
\]

## Conclusion

There are infinitely many n>N such that for every integer j with 1<=j<=K,

\[
T^j(n)\equiv n\equiv-1\pmod q,
\qquad
V(T^j(n))-V(n)>j\log(3/2)>0.
\]

Consequently there are no choices of q,K,N,h for which every n>N admits a j in {1,...,K} with V(T^j(n))<V(n). This excludes only this proposed sufficient descent scheme, not the Collatz conjecture or schemes allowing unbounded return times or other size-dependent corrections.

## Proof

For a positive integer t set n=2^(K+1) q t-1 and, for 0<=j<=K, set

\[
n_j=3^j2^{K+1-j}qt-1.
\]

All n_j are positive odd integers: K+1-j>=1, and n_0>=3. Also q divides n_j+1, so every n_j has residue -1 modulo q, including when q is odd or divisible by 3. No coprimality hypothesis is used.

We have n_0=n. If 0<=j<K and T^j(n)=n_j, oddness gives

\[
T(n_j)=\frac{3n_j+1}{2}
=3^{j+1}2^{K-j}qt-1=n_{j+1}.
\]

Induction therefore proves T^j(n)=n_j for the entire required window. Rewriting the expression gives

\[
n_j=(3/2)^j(n+1)-1
     =(3/2)^j n+((3/2)^j-1).
\]

For j>=1 the last summand is strictly positive. Thus n_j/n>(3/2)^j. The residue correction cancels exactly, and strict monotonicity of the logarithm yields

\[
V(n_j)-V(n)=\log(n_j/n)>j\log(3/2)>0.
\]

Taking arbitrarily large t makes n>N and supplies infinitely many distinct witnesses. Since q,K,N,h were arbitrary, the proposed certificate fails even when its return time j may vary with n inside the fixed window.

For context, that certificate would have been sufficient if the finitely many starts up to N were separately shown to reach 1. Indeed h has a minimum m, so V(u)<=V(n) implies u<=exp(V(n)-m), giving a finite sublevel set. On an orbit avoiding {1,...,N}, repeated applications of the proposed certificate would produce infinitely many strictly decreasing V values at endpoints in this finite set, a contradiction. This explains the downstream use of the rejected intermediate target; it does not assume that the certificate exists.

The witnesses depend on K. The formula gives no fixed positive integer with an infinite growing orbit. Increasing K, or considering compatible residue conditions at every depth, cannot silently replace this finite-window statement by a counterexample to Collatz.

Verification detail: `python3 scripts/finite-window/check_obstruction.py` checks the identity against direct integer iteration for q=1,...,32, K=1,...,24 and t in {1,2,3,17}. It checks parity, residues, and the strict ratio inequality using integers. These checks catch indexing errors; the induction above proves the unrestricted statement.

## Mathlib

Full statement: **not checked**. Supporting arithmetic and logarithm results: **not checked**; no theorem names or direct library links were verified. The proof is elementary and self-contained, and makes no claim of novelty.
