repeat_test
===========

A python script to test code for improperly repeated lines.


    Usage:
        python repeat_test.py <fileName> [outlierFactor=1]
        
    The outlier factor is the number of sigmas away from the mean the repeating lines
    difference must be to trigger a positive result.


Here's some of the output from the test file found (<a href="http://www.viva64.com/en/b/0260/print/">source</a>):


    ...
    Length: 4
    175)	pattern-&gt;patternRepeatY = true;
    177)	pattern-&gt;patternRepeatX = true;
    179)	pattern-&gt;patternRepeatY = true;
    181)	pattern-&gt;patternRepeatY = false;

    Length: 3
    176)	} else if (repetition == QStringLiteral("repeat-x")) {
    178)	} else if (repetition == QStringLiteral("repeat-y")) {
    180)	} else if (repetition == QStringLiteral("no-repeat")) {

    Length: 3
    191)	const int jstride = sizeof(tmp[0][0]) / sizeof(tmp[0][0][0]);
    192)	const int mistride = sizeof(mag[0]) / sizeof(mag[0][0]);
    193)	const int mjstride = sizeof(mag[0][0]) / sizeof(mag[0][0]);</code>
    ...

