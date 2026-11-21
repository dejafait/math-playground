# Reflected-prefix TEST — working record, step189

Approved scope: the exact TEST in the unchanged step187 assessment,
separately approved in step188. Main gap: L966(16), R_n<=N_n for every
index, feeding the audited L968 implication. The partial target is the
fixed reflected prefix and h charge; complementary arcs remain open.

Continue with a uniform bound or a discriminating rigorous intermediate
bound; one strict violation at n>=2 and 0<theta<=pi/4 retires this fixed
pairing/allocation. No changed radius, onset, or further finite Q sign.

Inputs read: L966 in full, L019, L970's moment setup (comparison only),
and the reused step186 local duplicate/failure comparison. L967/L969/
C969a concern different pointwise payments. No cross-notebook input.

Partial reasoning saved before numerical work: apply DLMF1.9.30-31 to
G on |x-b|=rho=1/2. With m=k-1, dx=i*rho*exp(it)dt cancels the
coefficient denominator to give G^(m)(b)/m! as the circle average
of G(b+rho*exp(it))*rho^(-m)*exp(-imt). For m=0 use 1.9.30.
Conjugation makes the upper-circle real integral equal this average.
Summing the finite real d_k yields exactly the Bell sum in L966(12),
without the h term. Multiplicities are already retained in L966.

Next within this attempt: bounded numerical localization of a possible
negative prefix, followed by a proof controlling the complete G on the
arc. A constant-G screen alone cannot certify TEST. A promising possible
error bound is the local product resolvent estimate from L024/L026;
it must be proved with actual complex paired nodes, not RH.

No inequality or certified failure has yet been established. All
numerical screens are diagnostics until a complete error argument exists.

## Preserved candidate obstruction before certification

The diagnostic `scripts/li-theta/reflected-prefix-screen-189.json`
selects n=18, theta=1/2. Put M=sum_k d_k*2^(k-1), g=G(b)>0,
and c_j=1/(alpha_j^2+b). From L026, writing alpha=a+ic gives
Re(alpha^2+b)>a^2>16 and |Im(alpha^2+b)|<|a|. Hence
|c_j|<1/16 and |c_j|<=(33/32)Re(c_j). Absolute convergence
gives sum|c_j|<=(33/32)g. On |delta|=1/2 the resolvent identity
therefore bounds |G(b+delta)-g|<=(33/992)g, with no real-zero
assumption. Triangle bounds for both entire W factors give full-prefix
error at most 2*theta*(33/992)*g*M/pi.

Writing A_m=d_(m+1)*2^m, the exact constant part is
S=2*d1*theta+2*sum_(even m>=2) A_m*sin(m*theta)/m.
At theta=1/2, S=d1+sum_(j=1)^8 A_(2j)*sin(j)/j.
The diagnostic gives S/M approximately -0.0688113, below the
negative-error threshold -33/992. Next: certify every sine value
by rational Taylor bounds and write a full canonical proof if successful.
No h estimate is needed for a negative-prefix counterexample: the exact
charge d1*G(64*9^18)/pi is strictly positive by L966, so it is retained
and makes the TEST margin still smaller.

## Completed disposition

The exact certificate succeeded with all 13 checks. Full proof and
qualifications are canonical in L971; the completed outcome is NEGATIVE
for the fixed TEST. The two paragraphs above preserve the reasoning
before certification, not a competing current-status record. PROGRESS.md
contains the sole current next action. Independent audit remains pending.
