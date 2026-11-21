# Compatible diagonal data do not make the averaged extension nonnegative

2026-11-06. The canonical proof and complete numerical qualifications
are in [L848](../lemmas/L848-actual-g-exchange-diagonal-compatible-data.md),
accepted by the separate conceptual audit of 6 November2026. Its actual-G diagonal data pass the
all-m test with K/C>4e-16. This failure concerns only extension (6).

**WHY IT FAILS.** The symmetric average of h and sine interpolation of
the normal derivative b has Du=0 at (0,pi), with opposite points
z_1=-z_2=sqrt(200000). The complete density there is
q/C=-G(sqrt(200000))G(-sqrt(200000))/50000. The qualified actual-G
interval evaluator certifies -4.546e-8<q/C<-4.545e-8. Thus exact
diagonal phase cancellation does not extend automatically to a global
positive contour. The earlier stronger Re(G/z)>0 circle test also
fails, while L848's wider sector succeeds; both records are retained.
Neither failure rules out other extensions preserving the same jets,
arbitrary exchange-equivariant graphs, or coupled graphs in general.
Any renewed construction needs a changed off-diagonal mechanism and
an everywhere-real/nonnegative test, not another diagonal phase plot.
