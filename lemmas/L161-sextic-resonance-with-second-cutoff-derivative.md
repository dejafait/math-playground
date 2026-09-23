# Lemma 161: sextic resonance with second cutoff derivative

**Hypotheses.** Use the finite window, positive amplitudes A_n, Q, U,
C² cutoff χ, M>0 and normalized expectation E_T of L160. Set θ=t−π/2.
The phase derivative means differentiating exponentials while holding
amplitudes fixed. Define

P=Σ_(a≠b) i log(a/b) A_a A_b exp(iθ log(a/b)),
Q_amp=Σ_(a,b) (A_a A_b)' exp(iθ log(a/b)).

Then Q'=P+Q_amp. For ordered sextuples in I define

W(t)=Σ_(a≠b,r≠s,m≠n,arm=bsn) A_a A_b A_r A_s A_m A_n.

**Conclusion.** The exact zero-total-frequency part of P U is

(P U)_res=W/2≥0.                                         (1)

Consequently L160's derivative remainder has the exact decomposition

R_der= E_T[χ''(Q/M)W]/(2M²)
       +E_T[χ''(Q/M)(P U)_non]/M²
       +E_T[χ''(Q/M)Q_amp U]/M².                        (2)

Here “res” selects zero frequency in the bare sextic expansion, before
multiplication by χ''. It is not a projection of the full weighted
integrand. If I contains three distinct indices, W>0. Thus the pointwise
sign of the first integrand in (2) is precisely that of χ''(Q/M).
The cutoff hypotheses do not provide a fixed sign for this factor.
No sign or uniform bound for its time average for the actual Gaussian
window and fixed M is established here.

**Proof.**

All sums are finite. Write x=log(r/s), y=log(m/n), z=log(a/b),
and p_6=A_a A_b A_r A_s A_m A_n. The definition of U gives

P U=Σ_(a≠b,r≠s,m≠n,rm≠sn)
       [z/(x+y)] [(x/y+y/x)/2] p_6 exp(iθ(x+y+z)).        (3)

The factors i cancel with positive sign. Resonance means arm=bsn,
or x+y+z=0. All three gaps are nonzero, so on this domain x+y=−z
is nonzero automatically. The coefficient in (3) is therefore
−h(x,y), where h(x,y)=(x/y+y/x)/2.

Permuting the three ordered pairs (r,s),(m,n),(a,b) preserves this
domain, all amplitudes, and ordered multiplicities. In particular each
choice of which pair supplied P gives the same total sum after a
bijection of indices. Average these three representations. For nonzero
x,y,z with x+y+z=0,

2[h(x,y)+h(x,z)+h(y,z)]
 = (x+y+z)(1/x+1/y+1/z)−3=−3.

Thus the averaged coefficient is −(−3/2)/3=1/2, proving (1).
This averaging remains valid with repeated pairs; it averages bijections,
not distinct unordered orbits. Positivity of the amplitudes gives W≥0.
For three distinct indices u,v,w, the pairs (u,v),(v,w),(w,u) give
an allowed strictly positive term, hence W>0. With fewer indices the
formula still holds without a strict positivity assertion.

Splitting Q' and (3) and retaining the common cutoff factor proves (2).
Conjugate pairing reverses all three pairs, so both the resonant and
nonresonant parts are real.

For completeness any permitted χ has χ'' of both signs in (1,2).
Indeed χ'(1)=χ'(2)=0 and ∫_1^2 χ'(v)dv=1, so χ'(c)>0 for some
c in (1,2). Applying the mean value theorem to χ' on [1,c] and
[c,2] gives a positive and a negative value of χ'', respectively.
For the explicit cutoff in L160, writing v=q−1 in (0,1),
χ''(q)=60v(1−v)(1−2v). At any t with Q(t)>0 and W(t)>0,
choosing M=Q(t)/q at either such q yields either sign of the weighted
resonant integrand. This is a pointwise statement as M varies, not a
claim of either sign for the integrated expression at a prescribed M.
Neither unweighted frequency orthogonality nor positivity of W removes
the cutoff correlation. ∎

## Verification

The proof uses only L160's finite expressions and hypotheses. Verify the
i cancellation, resonance exclusions, the three permutation bijections,
and the chain-rule decomposition of Q'. The regression
`python3 scripts/heat/check_sextic_resonance.py` uses integer frequencies
and exact rational coefficients to check the collected identity for
several finite sets and positive amplitudes. It checks the universal
finite algebra, not a Gaussian asymptotic or a zeta-zero statement.
The fixed-cutoff
tail target and RH remain unproved.

**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
