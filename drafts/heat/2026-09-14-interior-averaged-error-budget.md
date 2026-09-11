# Interior averaged error budget — checkpoint

The current test is restricted to L221's A times J, retaining all c,d.
No signed cancellation estimate is proved. Define B_box by summing
L220's uniform 8-bound with the absolute Möbius coefficients, before
bounding the k sum harmonically. Then |E_box|<=B_box.

Planned analytic audit: D(m)<=d(m) and divisor pairing give
sum_(m in J) D(m)<=2 sum_(r<=sqrt(max J)) (|J|/r+1)
=O(h log N+N)=O(h log N). Hence B_box=O(N³h log² N).
The k=j=1 coefficients and L221's coprime pair count give
B_box>=c N³h/log N. Meanwhile M_box is between
c N²h/log² N and C N²h. Thus the averaged uniform-error budget
still exceeds the main term by at least N/log N. This is a
limitation of this budget, not a lower bound on |E_box|.
Resume by checking restriction notation, divisor pairing and the
ratio, then store the method obstruction and a precise signed next test.

Completed as L222. Divisor pairing handles the short interval with
O(N) endpoint cost. The ratio is a lower bound on the uniform
budget only; actual signed cancellation is explicitly unproved.
