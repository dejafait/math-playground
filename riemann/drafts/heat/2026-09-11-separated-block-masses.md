# Draft: separated finite block masses — 2026-09-11

For finite integer blocks [a_j,b_j] with a_(j+1)>=4b_j, write
w_j=sum_(l=a_j)^b_j M_l/l^2 and A=sum w_j<infinity. Choose increasing
J_h with sum_(j>J_h) w_j<=2^-h. Put P(k)=1+sum_h 1_(b_(J_h)<k)
and F(k)=P(k)+1-1/(k+1). P is constant on each block, and endpoints
are at least quadrupling. Nonnegative interchange bounds the extra
weighted P sum by A+1; baseline integrability follows from logarithmic
growth. For k<l<2k at an extra mass, earlier endpoints are at most
a_j/4<=l/4<k, while its own endpoint is >=l. Thus P(l)=P(k), and
the near extra sum is <=2A. Near baseline <=4; far sum <=4D.

Checkpoint: draft claims are not yet proved inputs. Resume by checking
all block boundaries, arbitrary block widths, tail thresholds and the
L111 bounded-generator cutoff. In particular b_j<=2a_j appears unused;
retain the interblock separation and verify that dropping the width
condition does not affect any estimate. Earlier work is preserved.

Audit completed: the proof is stored in Lemma 115. The width restriction
is unused; preceding endpoints are below k at every near mass location
even for arbitrarily wide blocks. Both block endpoints, the empty near
range and l=2k were checked. The cutoff uses only its proved bounded-
generator component. This file retains the original draft checkpoint.
