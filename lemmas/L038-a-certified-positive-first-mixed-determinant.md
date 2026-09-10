# Lemma 38: a certified positive first mixed determinant

**Hypotheses.** The arithmetic contracts of Lemma 37 hold for the Python standard-library implementation. D and H_1 are as in Lemma 33.

**Conclusion.** The actual theta moments satisfy

3.38·10^{-15} < D < 4.34·10^{-15}.

In particular H_1 is positive definite. This is a computer-assisted finite partial result, not RH.

**Proof/certificate.** `scripts/hankel/certify_hankel.py` implements the explicit four-term theta integrands on [0,2], the eighth-order panel enclosure of Lemma 36, and the common tail of Lemma 35. It uses 70-digit outward arithmetic and the rational π enclosure of Lemma 37. The reproducible command is:

`python3 scripts/hankel/certify_hankel.py --panels 32 > scripts/hankel/hankel-certificate.json`

The saved output encloses S_2 in [0.0000371688839777867…, 0.0000371763145938135…] and D in [3.389399530870064…·10^{-15}, 4.331547435010644…·10^{-15}]. These ellipses abbreviate the exact rational decimal endpoints stored in `scripts/hankel/hankel-certificate.json`; the asserted looser bounds 3.38·10^{-15} and 4.34·10^{-15} contain those full endpoints strictly. The complete quadrature remainders and common tail enclosure are also saved there. The code propagates the full moment intervals through S_2,S_3,S_4 and then S_2S_4-S_3². By Lemmas 35–37, this interval contains the exact determinant. Its lower endpoint is positive, and S_2>0 is both analytically proved in Lemma 27 and enclosed positively here. Completing the square as in Lemma 33 proves positive definiteness.

Validation included exact rational containment checks for signed interval arithmetic, an exact exponential-derivative recurrence check at zero, and overlap with a separately evaluated expanded determinant expression. That second expression has a wider interval containing zero; the sign certificate uses the first, rigorously enclosing expression. No unvalidated decimal quadrature or zero computation enters the conclusion. ∎
