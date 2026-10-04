# L014 — Rational Kummer corrections cannot make the Kato family finite at p

## Hypotheses

Let E/Q be non-CM and let p >= 5 be a good ordinary prime. Assume
that rho_(E,p)(G_Q) = GL_2(F_p), the Manin constant
and every Tamagawa factor are prime to p, and E(Q_p)[p] = 0. Finiteness
of p-primary Sha and positive rational rank are not assumed. Some of
these hypotheses are stronger than the cited inputs need; they retain
the scope of the approved test.

Use Kim's auxiliary-prime set P, square-free indices N_1, coefficient
ideals I_n, fixed primitive roots, and local conditions from
[Sections 1.2.2 and 2.1--2.3, printed pages 4 and 11--13](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=11).
Write T = T_p E, R_n = Z_p/I_n and M_n = T/I_n T. For n = 1,
I_1 = 0, so these are Z_p and T. At finite coefficients, H_f^1
denotes the local Kummer image; at p, H_/f^1 is its quotient in H^1.
The n-modified condition is transverse at primes dividing n.
F_can is finite away from p and unrestricted at p; F_cl is finite
also at p. The auxiliary modification is the same for both structures.

Let kappa = (kappa_n) be Kato's ordinary integral Kolyvagin system for
(T,F_can,P), with all its coefficient reductions and finite-singular
relations. The zero local-torsion assumption permits the ordinary
system in Kim's Theorem 2.1: H^0(Q_p,E[p^infinity]) = 0 is divisible.
The system type here is the ordinary one in Section 2.2.2, not an
arbitrary partial array or a different rank-zero system.

For each n let c_n be in the rational Kummer image

\[
\mathcal K_n=\operatorname{im}\bigl(E(\mathbf Q)\otimes_{\mathbf Z}R_n
             \longrightarrow H^1(\mathbf Q,M_n)\bigr),
\qquad \kappa'_n=\kappa_n-c_n.
\tag{1}
\]

For c_1 the map is the inverse-limit Kummer map. Require the corrected
family to be of the same complete ordinary integral kind, with the
same coefficient reductions, every n-transverse local condition,
and every finite-singular equation for (T,F_can,P).

For the nonvanishing test, additionally assume a minimal nonzero
mod-p Kurihara index n_0 = ell_1 ell_2 with distinct auxiliary primes:
bar(delta_tilde_(n_0)) != 0. Minimality and the two-prime count are
test premises, not consequences of analytic order two.

## Conclusion

Every c_n = 0 for a complete correction family satisfying the above
relations and local conditions. Moreover, already for an isolated
rational Kummer correction at n_0,

\[
\operatorname{loc}_p^s(\overline{\kappa'_{n_0}})
 =\operatorname{loc}_p^s(\overline{\kappa_{n_0}})\ne0
 \quad\text{in }H^1_{/f}(\mathbf Q_p,E[p]).
\tag{2}
\]

Thus rational Kummer subtraction cannot make every component finite
at p while preserving the required nonzero mod-p component. The
full-family zero assertion uses the ordinary integral system; the
single-index obstruction (2) needs no relation-preservation premise.
In fact (2) holds at any index with a nonzero mod-p Kurihara value.

This stops the proposed correction mechanism. It establishes no
rational-rank lower bound, no rational determinant membership, and no
compatibility or incompatibility of the entire arithmetic family with
the formal marking in L013. No BSD counterexample is asserted.

## Proof

**Apply the classical-system theorem to the difference.** Kummer
localization commutes with the rational-to-local point map. Therefore
loc_v(c_n) is finite at every place v, including p, at every relevant
coefficient level. Away from primes dividing n this is the F_cl
condition. At a prime dividing n, both kappa_n and kappa'_n are
transverse by hypothesis. Their difference c_n is transverse too.
Consequently c_n satisfies F_cl(n). This verifies the actual auxiliary
condition, rather than replace it by the usual finite condition.

Fix ell not dividing n. Express both finite-singular equations in
M_(n ell), reducing the n-component from M_n where needed. Subtraction
gives

\[
\operatorname{loc}_\ell^s(c_{n\ell})
 =\phi_\ell^{fs}\bigl(\operatorname{loc}_\ell(c_n\bmod I_{n\ell})\bigr).
\tag{3}
\]

Here phi_ell^fs is the same finite-to-singular comparison as for
kappa. It applies since ell does not divide n, so the right side is
finite before comparison. The left side is zero since c_(n ell)
is Kummer at ell. The equation is preserved, not a new choice of
relations. Subtraction preserves all stipulated coefficient reductions
as well. Thus c is an ordinary integral Kolyvagin system for
(T,F_cl,P).

Kim's [Theorem 2.5(1), printed page 14](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=14)
gives KS(T,F_cl,P) = 0 under p >= 5 and surjective E[p]. Apply that
statement by citation to obtain c = 0, hence every component c_n = 0.
Its core rank zero concerns this Selmer structure, not rational rank.
This argument does not identify a completed core-rank-zero module
with the ordinary module, or assert vanishing of Sakamoto's differently
indexed rank-zero systems.

**The p-local obstruction does not require a whole family.** At any
finite-coefficient index n, let q_(p,n) be the local quotient map
H^1(Q_p,M_n) -> H^1_/f(Q_p,M_n). For any c_n in (1), Kummer
functoriality gives

\[
q_{p,n}(\operatorname{loc}_p c_n)=0,
\qquad
q_{p,n}(\operatorname{loc}_p\kappa'_n)
 =q_{p,n}(\operatorname{loc}_p\kappa_n).
\tag{4}
\]

No cancellation is possible in this quotient, regardless of the
rational points chosen for c_n.

Use the normalized torsion dual exponential Theta_n = xi_n exp*_omega
on this singular quotient in Kim's
[Proposition 3.10 and diagram (3.3), printed pages 19--20](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=19).
His [Theorem 3.11, printed page 20](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=20)
states the reciprocity value

\[
\Theta_n(q_{p,n}(\operatorname{loc}_p\kappa_n))
 =u_n p^t\widetilde\delta_n\in R_n,
\qquad u_n\in R_n^\times,
\tag{5}
\]

where, in this good-reduction case, p^t is the size of
E(Q_p)[p^infinity]. The assumption E(Q_p)[p] = 0 implies t = 0:
any nonzero p-power torsion point would yield one of order p.
Hence the value at n_0 in (5) is a unit modulo p.

The reduction of the singular quotient used here is the genuine
mod-p quotient. Indeed the local-torsion term H^2(Q_p,T)[I_n] in
Kim's (3.2) is zero by local Tate duality and E(Q_p)[p^infinity] = 0.
His description of H_f^1 as the propagated Kummer image then gives

\[
H^1_{/f}(\mathbf Q_p,M_n)
 \simeq H^1(\mathbf Q_p,T)\big/
 \bigl(I_n H^1(\mathbf Q_p,T)+H_f^1(\mathbf Q_p,T)\bigr).
\tag{6}
\]

The integral quotient is free of rank one, as in the proof of
Proposition 3.10. Its reduction modulo p is H^1_/f(Q_p,E[p]);
the exponential-lattice normalization xi_n is a rank-one lattice
trivialization and can be chosen compatibly with this reduction.
Thus a unit value in (5) has nonzero image in the mod-p singular
quotient. Equation (4) proves (2). Equivalently, finiteness of
bar(kappa'_(n_0)) would force that value to be zero, contradicting
bar(u_(n_0)) bar(delta_tilde_(n_0)) != 0.

The first argument rules out a nontrivial full rational correction
preserving the original system. The second rules out p-finiteness
already at the chosen index even without such compatibility. Neither
uses minimality or the count of index primes beyond identifying the
conditional test case. The required r >= 2 and the separate rational
determinant comparison therefore remain missing.

The theorem inputs and their exact local conditions were already
assessed in the saved SPECIALIZE review. This is their applicability
argument, classified as reproduction of known mathematics; no result
beyond the checked literature is claimed. No numerical calculation or
additional mathematical script is needed.

## Mathlib

Full coverage of this rational-correction obstruction: **not checked**.
Supporting Kummer maps, transverse conditions, finite-singular
comparison, local Tate duality and torsion dual exponentials:
**not checked**. Kim's Theorem 2.5(1) matches the classical ordinary
system vanishing input; Proposition 3.10 and Theorem 3.11 support the
single-index singular-value test. They are precise arithmetic
citations, not claimed Mathlib matches or rational determinant
theorems. No absence inference is made.
