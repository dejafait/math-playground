# Attempt: strict kernel log-concavity forces real Fourier zeros

Date: 2026-09-09

Outcome: failed general sufficiency claim; strict log-concavity of the actual theta kernel remains proved.

Lemmas 45–48 establish the full theta kernel's smooth even extension, strict decrease on u>0, and the quantitative bound (log K)''<-(68/125)πe^{2|u|}. The attempted shortcut was to invoke strict log-concavity by itself as a reason for real transform zeros.

For g=e^{-u²}, the mixture h=(9/10)g+(g(u-1/2)+g(u+1/2))/20 has (log h)''≤-1, by factoring off e^{-u²} and bounding the remaining slope variance by 1. Its transform is √πe^{-z²/4}(9+cos(z/2))/10 and has a nonreal zero at 2π+2i log(9+√80). Its fourth cumulant is 7/1600, giving T_2=-7/19200 despite strict log-concavity.

**WHY IT FAILS.** Strict log-concavity controls the shape of the real kernel but does not prevent complex phase cancellation in its Fourier transform. This smooth positive even strongly log-concave example has explicit nonreal zeros and a negative logarithmic sign. It has Gaussian decay and entire order two, so it does not disprove a more restrictive theorem combining log-concavity with the actual theta-scale tails and order-one growth. Those extra hypotheses must be analyzed rather than silently discarded or assumed sufficient.

Next lemma: test the combined conditions by a small-shift mixture of the superexponential base exp(-cosh(2u)), proving or disproving preservation of log-concavity quantitatively before drawing any conclusion.
