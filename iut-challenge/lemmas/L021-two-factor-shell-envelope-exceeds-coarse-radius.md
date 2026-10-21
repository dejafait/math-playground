# L021 — The assumed two-factor shell envelope exceeds the coarse radius

## Hypotheses

Retain exactly L020's auxiliary packet: K=Q_3(pi), pi^27=3, v(3)=1, J=log(O_K^times), I=J/6, the tensor family (K,Q_3), a=pi tensor 1, beta=1, and h=g tensor identity for L017's fixed involution. Write mathcal I for the tensor shell and mu for L020's multiplication identification with K. Thus mu(mathcal I)=I, mu h mu^(-1)=g, and the prescribed coarse radius is 81. L020 establishes shell preservation and the scalar/conductor qualifications after factor exchange.

Test only the assumed first-power envelope E=a mathcal I. Its motivation is **Dupuy–Hilado, arXiv:2004.13228v1 (2020-04-28), §4.9, equation (4.3), printed p. 23**, followed by §4.10's subsequent indeterminacies ([versioned primary PDF](https://arxiv.org/pdf/2004.13228v1#page=23)). This is an auxiliary first-power analogue of the explicitly assumed positive-power envelope, not an identification with actual ind3 images or a specialization of original pilot data. The coarse prescription is **Dupuy–Hilado, arXiv:2004.13108v2 (2020-04-29), §6.2, unnumbered formula after (6.8), printed p. 20** ([versioned primary PDF](https://arxiv.org/pdf/2004.13108v2#page=20)), already specialized in L020.

L017 establishes, on the complete actual logarithm image, g(pi J) subset I/9, min v(I)=-3, and an actual q in J with v(q)=-2 and g(pi q)=q/54. It also proves log(1+pi)=q+t with v(g(pi t))>=-2. These are reused established inputs, without recomputing the logarithm lattice or assuming O-module stability.

## Conclusion

The complete fixed envelope image has sharp field radius

\[
\operatorname{hull}(\mu(h(E)))=\pi^{-162}O_K,
\qquad R=3^6=729>81.
\]

The envelope point (pi q/6) tensor 1 maps to (q/324) tensor 1. Its field valuation is -6, strictly below the required -4. Thus the assumed first-power envelope alone does not ensure radius 81 under this fixed auxiliary shell-preserving map. This does not exhibit a point of actual ind3 images or an essential IUT flaw.

## Proof

Multiplication by a under mu is multiplication by pi. Hence mu(E)=pi I=pi J/6. The element q/6 belongs to I because q is an actual member of J, so x=(pi q/6) tensor 1 belongs to E. Membership is in the specified shell envelope, rather than in L020's smaller literal input.

The scalar 1/6 is rational. Q_3-linearity, applied after the tensor identification, gives the complete-set identity and inclusion

\[
g(\pi I)=\frac{1}{6}g(\pi J)
\subseteq\frac{1}{6}\frac{I}{9}=\frac{I}{54}.
\]

No commutation with multiplication by pi is used: the established input is the image of pi J itself. Since v(54)=3 and every element of I has valuation at least -3, every element of the fixed image has valuation at least -6. This proves enclosure of all of E, not just its selected point. It asserts containment in I/54, not equality with that lattice.

For the specified envelope point, the established exact image gives

\[
\mu(h(x))=g(\pi q/6)=\frac{q}{6\cdot54}=\frac{q}{324}.
\]

Here 324=4\cdot3^4, so v(q/324)=-2-4=-6. The upper bound is attained. With v(pi)=1/27, the smallest centered closed field disc is therefore pi^(-162)O_K. Its radius for |y|_3=3^(-v(y)) is 729. The radius-81 disc is pi^(-108)O_K, with valuation threshold -4; the witness is strictly outside it. The ratio of radii is exactly 729/81=9.

There is also an envelope witness using the original convergent logarithm: (pi log(1+pi)/6) tensor 1 belongs to E because log(1+pi)/6 belongs to I. Its image is q/324+g(pi t)/6. The complete tail bound gives v(g(pi t)/6)>=-3>-6, so cancellation cannot alter the sharp valuation -6. No finite approximation is substituted for the infinite logarithm.

This result is compatible with L020: its literal logarithm branch is 3pi J, and pi I=(1/18)(3pi J). Rational scaling by 1/18 raises that branch's sharp image radius from 81 to 729 because |1/18|_3=9. The stopped literal-union objection remains stopped. The enlarged envelope is the separately assessed premise; its excess cannot be transferred to actual images merely from an assumed containment of actual images in that envelope.

The calculation uses only complete inclusions, an exact established image, rational linearity and exact valuations. No new mathematical script or numerical sampling is needed. The prior SPECIALIZE assessment is `drafts/literature/2026-10-05-two-factor-shell-envelope-sufficiency.md`. Classification **POTENTIALLY_NEW** refers only to its bounded comparison: the inspected sources did not certify this fixed-envelope image, and originality is not established. Actual ind3 membership/equality, higher powers, original permitted-map realization, inter-summand permutations, initial theta data, pilot transport, essentiality and normalized finite B>=A remain unresolved. L019's full-pair exclusion of this g remains a scope restriction, not an admissibility input.

### Critical audit, 2026-10-06

The existing fixed-envelope conclusion survives this audit. This is verification of L021, not a new radius result or a certification of originality. The prior coverage is `drafts/literature/2026-10-05-two-factor-shell-envelope-critical-audit.md`; its source comparisons are reused without a new literature search.

**Input and map.** L020 identifies the second shell with Z_3 because log(Z_3^times)/6=(1/2)Z_3=Z_3. In particular 1 belongs to that shell, so the displayed tensor witness is legitimate. The multiplication map identifies the whole tensor shell with I and conjugates h to g. Tensor symmetry puts pi in the required last factor; beta=1 satisfies both conductor conditions. The coarse constant is 27/|6|_3=81: the different contribution cancels and floor(1/27)=0. There is one field component. None of these identifications makes the tensor logarithm equal to J: its image remains 3J.

**Complete enclosure.** L017 proves pi J subset I/9 from 54pi J subset H subset J, and g preserves I/9 by Q_3-linearity and g(I)=I. This checks the complete-image input g(pi J) subset I/9 without using a sampled vector or whole-orbit equality. Dividing the entire image by 6 gives g(pi I) subset I/54. Since v(54)=3 and min v(I)=-3, the bound is -6 on every image point. Only the rational scalar 1/6 has moved through g; multiplication by pi has not. No O-module stability or equality g(pi I)=I/54 is needed.

**Attainment and actual logarithms.** L016's complete-image proof places H=pi^14 O inside J by the strict log/exp threshold 14/27>1/2, and puts log(1+pi)-q in H. Thus q is in J, rather than just a finite approximation. Its constant term 16/9 has valuation -2 and its other nonzero terms have strictly larger valuation. L017's integral splitting functionals interchange w=9pi q and z=q/6, giving g(pi q)=q/54. Consequently the envelope image q/324 has valuation -6, as 324=4*3^4. This attains the complete lower valuation bound, so the asserted centered field hull follows; it is not inferred from lattice content alone.

For the infinite-log error t in H, the full formula in L017 gives A(pi t) in 3^4 Z_3 and B(pi t) in 3Z_3. Since v(w-z)=-3 and v(pi t)>=15/27, it gives v(g(pi t))>=-2 for every t in H. After division by 6 the error has valuation at least -3, strictly above -6. This verifies noncancellation for the convergent logarithm, not only the exact representative. L016's tail argument covers every omitted series term, not a precision cutoff. The previously audited logarithm representatives and analytic estimates are reused as canonical inputs; no new logarithm theorem or finite-certificate claim is made here.

**Threshold and interpretation.** The attained valuation -6 is strictly below the radius-81 threshold -4. Independently, pi I=(3pi J)/18 and |1/18|_3=9 reconcile the radius 729 with L020's sharp literal-branch radius 81. The smaller-union stop is therefore preserved. The audit verifies a conditional auxiliary envelope diagnostic only. It gives neither actual ind3 membership for the witness nor a native permitted-map realization; the full-pair restriction in L019 remains intact. Higher powers, original data, pilot transport, essentiality and finite B>=A remain unresolved. No argument change, new direct mathematical dependency, script or additional lemma is required.

## Mathlib

Full fixed-envelope counterexample and field-specific sharp image: **not checked**. Supporting tensor identification, rational linearity, valuation and logarithm/lattice coverage: **not checked**. No absence claim is made. The primary citations fix the envelope premise and coarse prescription; L017 and L020 supply the already established exact local inputs.
