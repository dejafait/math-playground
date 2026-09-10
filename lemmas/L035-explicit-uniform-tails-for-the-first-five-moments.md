# Lemma 35: explicit uniform tails for the first five moments

**Hypotheses.** For n≥1 set K_n(u)=[8π²n⁴e^{9u/2}-12πn²e^{5u/2}]e^{-πn²e^{2u}}. For k∈{0,2,4,6,8} put B_k=∫_0²u^kΣ_{n=1}^4K_n(u)du.

**Conclusion.** 0≤M_k-B_k≤E, where the following explicit positive constant works for all five k:

E=128e^{-150}Σ_{j=0}^6 [6!/(6-j)!]50^{6-j}/3^{j+1} + 57,600,000e^{-74}.

**Proof.** Every K_n is positive on u≥0 by Lemma 19. Also u^k≤e^{8u} on u≥0 for the five stated k: for u≤1 use u^k≤1, and for u≥1 use log u≤u. For n≥1, n⁴≤16^{n-1} and n²≥1+3(n-1). Thus for X≥1,

Σ_{n≥1}n⁴e^{-πn²X}≤e^{-πX}/(1-16e^{-3πX})≤2e^{-πX},

using π>3 and e⁹>32. Dropping the negative term in each K_n and using π<4 gives u^kK(u)≤256e^{25u/2}e^{-3e^{2u}}. On u≥2 put X=e^{2u}; the resulting upper tail is at most 128∫_{e⁴}^∞X^{21/4}e^{-3X}dX. The exponential series through its seventh term gives e⁴>50. Since X^{21/4}≤X⁶ for X≥1, the tail is at most 128∫_{50}^∞X⁶e^{-3X}dX, which repeated integration by parts evaluates as the first term of E.

For the omitted n≥5 terms, integrate over all u≥0, an upper bound for their contribution on [0,2]. The same positive-term and π bounds give

Σ_{n≥5}∫_0^∞u^kK_n(u)du≤64Σ_{n≥5}n⁴∫_1^∞X⁶e^{-3n²X}dX
≤64·720Σ_{n≥5}n⁴e^{-(3n²-1)}.

The last inequality uses e^{-3n²X}≤e^{-(3n²-1)}e^{-X} for X≥1 and ∫_0^∞X⁶e^{-X}dX=720. Write n=5+j. Then n⁴≤625·16^j and n²≥25+11j for integers j≥0. Hence the last sum is at most 625e^{-74}/(1-16e^{-33})≤1250e^{-74}, giving the second term of E. The two upper bounds may overlap, which only enlarges their sum and is harmless. ∎
