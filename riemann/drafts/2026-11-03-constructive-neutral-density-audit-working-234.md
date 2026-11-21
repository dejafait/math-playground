# Constructive neutral density — audit working record, step 234

The preexisting SPECIALIZE assessment is the supplied gate for exactly
paper 18/v3 (33),(43)--(44), with complex fixed vectors. L729 and its
working/history notes were read; density was expressly excluded there.
The primary source still displays v3 (22 October 2026). Its definitions,
(27)--(28), (33), and complete (43)--(44) were retrieved for this replay.
No new literature assessment or changed mathematical scope is invoked.

Endpoint check in progress: integrate f_m/y to Y=mq. Finite floor-cell
summation gives

    -q log m-log(q!)+(1/m)log((mq)!)+a_m log(mq).

Stirling's formula gives (log m)/2-a_m log(2pi). L729's bounded
primitive justifies the ordinary improper limit and all other endpoints.
The finite floor(y)f_m/y^2 identity then gives (28), without using the
prime representer or the source's contour proof.

With h_m=<fractional-part,rho_m>, ||rho_m||<=sqrt(2/m), |h_m|<=sqrt(2/m),
T_m(1)=(log m)/2-c_0 a_m-h_m. For R=floor(K/2), S=K, the determinant
equals (log(S/R))/4-log(S)/(4R)+log(R)/(4S)-a_R h_S+a_S h_R.
It tends to (log 2)/4 through even and odd K. Cramer's rule gives
complex repair coefficients O(|A(u)|log K+|B(u)|); the norm cost tends
to zero for each fixed u. Pending: canonical full proof, closure and
documentation check. No unit-ball statement or full norm estimate.

Completed: the full replay passes and is canonical in L730. It includes
well-definedness from L729's jump inversion and the closure argument.
No source contour or prime-representer theorem was imported. This
working record preserves the preliminary reasoning only.
