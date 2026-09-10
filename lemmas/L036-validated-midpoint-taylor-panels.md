# Lemma 36: validated midpoint Taylor panels

**Hypotheses.** f is real C⁸ on [c-h,c+h], h>0. For j=0,…,7 write a_j=f^{(j)}(c)/j!, and suppose B≥sup_{u∈[c-h,c+h]}|f^{(8)}(u)|/8!.

**Conclusion.**

|∫_{c-h}^{c+h}f(u)du - 2Σ_{j=0}^3 a_{2j}h^{2j+1}/(2j+1)| ≤ 2Bh⁹/9.

Interval enclosures of the coefficients and B give an enclosure of the integral by interval addition and multiplication.

**Proof.** Taylor's theorem with integral remainder (or the Lagrange bound applied pointwise) gives |f(c+t)-Σ_{j=0}^7a_jt^j|≤B|t|⁸ for |t|≤h. Integrate this bound. Odd monomials integrate to zero, even monomials integrate to 2h^{j+1}/(j+1), and ∫_{-h}^h|t|⁸dt=2h⁹/9.

For implementation, normalized derivative coefficients of a product obey (fg)_n=Σ_{j=0}^n f_jg_{n-j}. If b=exp(a), its coefficients obey b_0=exp(a_0) and b_n=(1/n)Σ_{j=1}^n j a_jb_{n-j}, by differentiating b'=a'b and comparing coefficients. These identities hold at every point of a panel. Evaluating them by enclosing interval operations with the variable's constant coefficient equal to the full panel and its first coefficient equal to 1 therefore encloses f^{(8)}(u)/8! uniformly. Evaluating at the midpoint encloses the lower coefficients. The finite theta integrands are smooth by their explicit exponential formulas, so these operations apply. ∎
