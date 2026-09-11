# Mellin contour audit checkpoint — 2026-09-12

Current step, initially unproved: Gaussian Mellin inversion should give
D(s;A)=sqrt(pi)/(2 pi i) integral_(c) exp(w²/4) A^w zeta(s+w) dw,
c>1-Re(s). At s=-1+i tau shift to Re(w)=0, crossing w=2-i tau.
The candidate residue is sqrt(pi) A^(2-i tau) exp((2-i tau)²/4),
with modulus sqrt(pi) A² exp(1-tau²/4). It cannot dominate sqrt(t).

Resume by proving Gaussian inversion and absolute interchange, obtaining a
polynomial vertical-strip bound sufficient for horizontal edges, and bounding
the new integral using the functional equation at Re(s+w)=-1. Expected
absolute bound O((1+tau)^(3/2)) does not yield a lower bound or resolve
cancellation at the sqrt(t) scale. No draft claim is a proved DAG input.

Completed in L145: inversion, interchange, contour shift, residue, and the
uniform absolute remainder bound are proved. No unfinished claim was promoted.
The oscillatory remainder's lower bound remains unproved.
