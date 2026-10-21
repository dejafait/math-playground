# L020 — Two-factor fixed involution meets the coarse enclosure sharply

## Hypotheses

Let K=Q_3(pi), pi^27=3, v(3)=1, O=O_K, J=log(O^times) and I=J/6. Use the complete actual logarithm image and q=q_1 in J of L016, and the fixed involution g of L017. In particular v(q)=-2, g(pi q)=q/54, min v(I)=-3, g(pi O) subset I, and g(pi J) subset I/9. These are established inputs, not conclusions inferred from sampled images.

Take K_1=K and K_2=Q_3. Write

\[
L=K\otimes_{\mathbb Q_3}\mathbb Q_3,\qquad
T=O\otimes_{\mathbb Z_3}\mathbb Z_3,
\qquad \mathcal I=I_{K_1}\otimes_{\mathbb Z_3}I_{K_2},
\]

where I_F=log(O_F^times)/6. Let a=pi tensor 1, beta=1 and h=g tensor id. The literal first-power input is

\[
M=a\bigl(O_L\ \cup\ (J\otimes_{\mathbb Z_3}
\log(\mathbb Z_3^\times))\bigr).
\]

Use **Dupuy–Hilado, arXiv:2004.13108v2, dated 2020-04-29 (PDF prints April 30, 2020)**: §2.2, (2.1), printed p. 6, for the monogenic different formula; Theorem 2.8.1 and Remark 2.8.2, pp. 9–10, for the conductor choice; Lemma 4.2.3(2) and Definition 4.3.1, pp. 17–18, for the logarithm and shells; and §6.2, (6.3) and the unnumbered coarse formula after (6.8), pp. 19–20, for the input and radius. [Primary versioned PDF](https://arxiv.org/pdf/2004.13108v2).

The prior SPECIALIZE assessment is `drafts/literature/2026-10-05-two-factor-degree-27-coarse-test.md`. Its scalar-placement qualification is essential: apply §6.2 to the reordered family (Q_3,K), with pi in the last factor, and transport back by tensor symmetry. This is a tensor identification, not an asserted original ind1 action. No original initial theta data or permitted-indeterminacy realization is assumed.

## Conclusion

The map h preserves the prescribed tensor shell. Beta=1 satisfies both the maximal-order conductor inclusion and the component-valuation constraint. Under the canonical identification L=K, the input is exactly

\[
M=\pi O\ \cup\ 3\pi J.
\]

The fixed image has sharp branch radii 27 and 81, respectively. Thus

\[
\operatorname{hull}(h(M))=\pi^{-108}O,
\qquad R_{\rm actual}=81=R_{\rm coarse}.
\]

Both an actual unit logarithm representative and the original infinite-log input attain radius 81. Consequently this fixed two-factor involution **does not violate** the prescribed coarse enclosure. This stops the approved tensor-witness objection, without resolving the original IUT comparison.

## Proof

### Exact tensor identifications and source applicability

The multiplication identification mu:K tensor_Q3 Q3 -> K sends x tensor c to cx; its inverse sends x to x tensor 1. It restricts to T=O and identifies the maximal order O_L with O. There is only one field component, so the hull is a field disc with no additional component norm.

Import Lemma 4.2.3(2): for e(F/Q_p)<p-1, log(O_F^times)=varpi_F O_F. Here F=Q_3, e=1<2 and varpi_F=3, so log(Z_3^times)=3Z_3. It is the unit logarithm, not an extension to arbitrary nonzero elements. Hence I_{K_2}=(1/2)Z_3=Z_3, because 2 is a 3-adic unit. Under mu the tensor shell is (1/2)I=I, whereas the tensor logarithm is 3J. Tensoring these rank-one free Z_3-modules introduces no kernel; multiplying by their generators gives these identifications explicitly. In particular the second logarithm factor cannot be discarded.

The conjugate of h under mu is g: rational linearity gives mu(g(x) tensor c)=c g(x)=g(cx). Therefore h preserves mathcal I because g(I)=I. The tensor symmetry to the reordered family sends h to id tensor g, a to 1 tensor pi, and transports both integral branches and the shell. The source's last-factor requirement is thus satisfied, and |a|_3=3^(-1/27)<1.

For completeness the cited monogenic formula gives Diff(K/Q_3)=(27pi^26), since O=Z_3[pi] and f(X)=X^27-3. Its valuation is d_1=3+26/27=107/27; the trivial extension has d_2=0. Thus sum d_i-max d_i=0. Independently, beta O_L=O=T verifies the conductor inclusion, and v(beta)=0 verifies its only component-valuation condition. This is the conductor choice omitting the wild factor in Remark 2.8.2; after factor exchange the omitted factor changes label. It need not be the derivative of the last factor. Both prescribed beta constraints are checked, rather than choosing a scalar from its valuation alone.

The printed coarse formula, with its single |2p|_p denominator, specializes to

\[
R_{\rm coarse}
=\frac{27\cdot1}{|6|_3}
3^{-\lfloor 1/27+\max(d_1,d_2)-(d_1+d_2)\rfloor}
=27\cdot3=81.
\]

This is the post-(6.8) coarse formula, not the m-dependent real constant in (6.8).

### Enclosure of both complete literal branches

The identified first branch is pi O. L017's genuine inclusion pi O subset I and preservation of I give g(pi O) subset I. Since min v(I)=-3, its image radius is at most 27.

The identified logarithm branch is 3pi J. L017 gives g(pi J) subset I/9. Rational linearity therefore yields

\[
g(3\pi J)=3g(\pi J)\subseteq I/3.
\]

Since min v(I/3)=-4, this branch has radius at most 81. This proves enclosure for all elements of both branches, not just the displayed witnesses. It uses no O-module invariance of J. Indeed the same upper inclusions hold for every shell-preserving map by L017's input inclusions, although the action tested here remains the fixed h.

### Attainment and the infinite-log tail

For the logarithm branch, L016 proves q in J. Thus pi q tensor 3 is an actual tensor input, identified with 3pi q. L017's exact image gives

\[
g(3\pi q)=q/18,\qquad v(q/18)=-2-2=-4.
\]

It attains radius 81, rather than the singleton image radius 243. Write log(1+pi)=q+t with t in H=pi^14 O. L017 proves v(g(pi t))>=-2 on the full H, including the convergent error. Consequently v(g(3pi t))>=-1>-4, so

\[
v\bigl(g(3\pi\log(1+\pi))\bigr)=-4.
\]

The actual infinite-log input also attains the boundary, with no possible tail cancellation.

For the ideal branch retain L017's w=9pi q and z=q/6, with v(w)=1/27 and v(z)=-3. Its involution is g(y)=y+(A(y)-B(y))(w-z), where A(y)=27c_0/8 and B(y)=-3phi(y)/496. On pi, A(pi)=0 and phi(pi)=-31/3, so B(pi)=31/496. This coefficient is a 3-adic unit, and

\[
g(\pi)=\pi-(31/496)w+(31/496)z.
\]

The first two summands have valuation at least 1/27; the last has valuation -3. Hence v(g(pi))=-3, proving the ideal radius exactly 27. The union's attained minimum is -4, so its smallest centered closed field disc is pi^(-108)O and its radius exactly 81.

### Verification and limitations

Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/coarse-ideal/check_two_factor_degree_27.py`. The full certificate is `scripts/coarse-ideal/two-factor-degree-27.json`. It parses all thirteen q_j from L016's canonical table; checks splitting values, integral shell functionals and the involution on all 27 power-basis vectors; and records exact images and valuations for all 27 ideal generators, all 40 logarithm generators and all 27 deep-tail generators. The sharp image is exactly q/18, all tensor logarithm images have valuation at least -4, all ideal images at least -3, and the tail bound is at least -1. There are zero failed finite checks. The proof/citations above, rather than finite sampling, establish complete logarithm coverage, tensor identifications, conductor admissibility and the infinite tail.

Classification is **REPRODUCTION**: this verifies the source-prescribed coarse enclosure for the approved packet and fixed map, importing the logarithm theorem and specializing established local inputs. It is neither a new general enclosure theorem nor a claim of originality. The stopped full-pair realization obstruction of L019 remains intact; tensor symmetry does not provide such a lift. Actual initial theta data, the full original permitted-image identification, ind3-to-literal-region identification, pilot transport, essentiality and normalized finite B>=A remain unresolved. A successful two-factor local enclosure neither proves nor refutes any of these bridges.

## Mathlib

Full fixed-packet tensor specialization, exact logarithm lattice and sharp enclosure: **not checked**. Supporting tensor symmetry/unit identifications, local logarithm, different, valuation and lattice coverage: **not checked**. The cited primary results support the stated imports; no matching full Mathlib theorem or absence from Mathlib is claimed.
