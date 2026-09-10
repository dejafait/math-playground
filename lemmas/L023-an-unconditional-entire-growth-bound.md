# Lemma 23: an unconditional entire growth bound

**Hypotheses.** Ξ is defined in Lemma 18 and R≥1. Write B(R)=max_{|z|≤R}|Ξ(z)|.

**Conclusion.** log B(R)≤C+(R/2+4)log(R/2+4) for a fixed real constant C. In particular Ξ has entire order at most 1, meaning limsup_{R→∞} log log(max(e,B(R)))/log R≤1.

**Proof.** Lemmas 19–20 give, for a fixed C_1>0,

B(R)≤C_1∫_0^∞exp((R+9/2)u-πe^{2u})du
=(C_1/2)∫_1^∞x^{a-1}e^{-πx}dx,

where a=(R+9/2)/2. Put m=ceil(a). For x≥1, x^{a-1}≤x^m and e^{-πx}≤e^{-x}, so the last expression is at most (C_1/2)Γ(m+1)=(C_1/2)m!. The gamma recurrence, obtained by integration by parts in Euler's integral, gives Γ(m+1)=m!. Since m!≤m^m and m≤R/2+13/4<R/2+4, the asserted logarithmic bound follows after enlarging the constant. The displayed order bound follows by taking two logarithms and dividing by log R. No zero-location information was used. ∎
