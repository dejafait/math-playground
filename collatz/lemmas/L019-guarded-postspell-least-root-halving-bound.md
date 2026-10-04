# L019 — Imported guarded postspell final-halving bound at a least bad root

## Hypotheses

For positive integers use the shortcut map

\[
T(x)=\begin{cases}x/2&x\text{ even},\\(3x+1)/2&x\text{ odd}.\end{cases}
\]

Let \(\mathcal B_{20}\) be the positive integers congruent to 20 modulo
27 whose shortcut orbit never reaches 1. If a nonconvergent positive
start exists, L014 supplies \(n=\min\mathcal B_{20}\). Hold this
original root fixed; its existence is a conditional premise.

Write O for an actual odd shortcut step and E for an actual even
shortcut step. Suppose the orbit of n has the actual prefix
\((OOEO)^J O^H\), where \(J\ge2\) and \(H\ge3\) are integers, and put

\[
z=T^{4J+H}(n),\qquad
e(J,H)=\min\{a\in\mathbb Z_{\ge0}:a\ge J+H,\ a\equiv2\pmod{18}\}.
\]

For a positive integer x, \(v_2(x)\) is the largest nonnegative
integer a with \(2^a\mid x\). An actual prefix means that every
letter is used only at its permitted input parity.

## Conclusion

The original least root necessarily satisfies

\[
\boxed{v_2(z)<e(J,H).}
\tag{1}
\]

Equivalently, no such least-root prefix can have a following even
tail of length at least e(J,H). This imports a sufficient descent
guard; it does not claim that this threshold is optimal, that every
root has the specified prefix, or that the remaining cases converge.

## Proof

### Precise cited forward input

Sodelin, *Guarded root descent after independently unbounded return
spells and odd runs*, node `AC-POSTSPELL-GUARDED-ROOT-DESCENT-001`,
[sections 1–3 of Postspell_Guarded_Root_Descent.md, web lines 25–151](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Postspell_Guarded_Root_Descent.md#1-uniform-original-root-margin),
gives the following two conclusions for this same shortcut map:

- If r>3 has actual prefix \((OOEO)^J O^H\), J>=2 and H>=3, with
  endpoint z, then \(0<z/2^a<r\) whenever \(a\ge J+H\) and
  \(2^a\mid z\).
- If additionally \(r\equiv20\pmod{27}\) and
  \(a\equiv2\pmod{18}\), the integral endpoint \(z/2^a\) is
  congruent to 20 modulo 27.

Section 1 proves the original-root margin; section 3 proves target
membership. The prior IMPORT assessment
`drafts/literature/2026-10-04-residue47-bounded-ancestor-cover.md`
read these statements and their proofs on 2026-10-04 from live main,
without an immutable revision identifier. Import the guarded theorem,
not any universal claim from the informal repository. No Lean build
or reproof of the margin is assumed here.

For the residue convention, one actual OOEO block obeys
\(16r'=27r+23\), so it preserves residue 20 since
\(16\cdot20\equiv23\pmod{27}\). After H odd steps from that residue,
\(2^H(z+1)=3^H(r'+1)\), and H>=3 gives
\(z\equiv-1\pmod{27}\). Finally,
\(2^{18}\equiv1\pmod{27}\) and \(4\cdot20\equiv-1\pmod{27}\).
These identities check applicability of the cited membership conclusion
to the local O/E conventions; they do not replace its size estimate.

### Final-even and fixed-root guards

Put s=J+H. With the remainder chosen in \(\{0,\ldots,17\}\),

\[
e=e(J,H)=s+((2-s)\bmod18).
\tag{2}
\]

This is the least integer at least s in the stated congruence class.
In particular e>=s>=5. The least residue-20 root has n>=20>3,
so the source's size hypothesis holds.

Suppose, contrary to (1), that \(v_2(z)\ge e\). Then for every
\(0\le i<e\), \(z/2^i\) is a positive even integer. Consequently
the next e shortcut steps are actual E steps, and

\[
m=\frac{z}{2^e}=T^{4J+H+e}(n)
\]

is a positive integer. The cited conclusions, applied at the original
root r=n and a=e, give \(m<n\) and \(m\equiv20\pmod{27}\).
Both the final-even guard and the strict comparison with the original
root have therefore been retained.

Minimality of n implies that m converges: otherwise m would be a
smaller member of \(\mathcal B_{20}\). Choose k>=0 with
\(T^k(m)=1\). Then \(T^{4J+H+e+k}(n)=1\), contradicting the
definition of n. This proves (1). This is forward convergence transfer;
no ancestor hitting-time case distinction is needed.

The theorem is invoked only after assuming divisibility. A formal
affine endpoint without the actual parity word, or with fewer than e
available halvings, cannot justify this contradiction. A smaller
endpoint outside residue 20 likewise would not follow from the chosen
least-root premise. No later root is substituted for n.

Exact modular arithmetic and three guarded trajectory replays checked
transcription, as recorded in
`drafts/2026-10-04-guarded-postspell-application.md`. The universal
size margin is the cited theorem, not those finite checks. This is
KNOWN_IMPORTED local progress, not a result beyond the inspected
literature or a complete candidate for Collatz.

## Mathlib

Full guarded postspell descent theorem and least-root bound: **not
checked**. Supporting valuation, congruence, iteration and
well-ordering coverage: **not checked**. No matching declaration or
library absence is asserted. The direct source citation above is a
mathematical input, not a claim of Mathlib coverage.
