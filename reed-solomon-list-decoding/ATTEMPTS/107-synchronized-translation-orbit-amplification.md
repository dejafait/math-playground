# Synchronized translation alone does not force a witness

WHY IT FAILS: [L132](../lemmas/L132-synchronized-translation-orbit-cover.md)
gives complete finite deletion rules hitting every synchronized candidate,
before incidence or signed-rank filtering. They delete 656915 left and
638146 right indices, below both budgets 1038857, and retain 1914438
and 1933207 supports. Thus rank filtering cannot rescue retention-only
forcing by this orbit. This is not a packed counterexample: cross-side
packing and witnesses outside the orbit are not checked. Reopening
requires an additional mechanism, such as independently translated
pairs coupled through cross-packing, and separate source assessment;
repeating enumeration of this synchronized orbit cannot change the cover.
