# Data from: http://www.ny1.com/content/top_stories/156599/now-available--2007-2010-nyc-teacher-performance-data#doereports

from pylab import *
from pandas import *
import re

def get_data(filename):
    d = read_csv(filename, delimiter="\t")
    d['teacher'] = d['teacher_name_first_1'] + " " + d['teacher_name_last_1']
    return d

d2009 = get_data('teacher_data_2009_2010.csv')
d2008 = get_data('teacher_data_2008_2009.csv')

# For whatever reason, the $%@$ NYC DOE couldn't be bothered to use the same data fields across years.
#Normalize subject
for d in [d2008, d2009]:
    d['subject'][d['subject'] == 'English Language Arts'] = 'ELA'
    d['subject'][d['subject'] == 'Mathematics'] = 'MATH'

#Normalize Grade
#Yes, grade can't be an integer. It is stored as the string '5th' in one year, and '5th grade' in the other year. WTF!
strip_grade_re = re.compile('(\d+).*')
for d in [d2009, d2008]:
    for i in range(len(d)):
        d['grade'][i] = int(strip_grade_re.match(d['grade'][i]).groups()[0])

def _get_grade_field(d):
    grade_field_finding_regex = re.compile('va_pctl_\d{4}')
    grade_fields = [ cl for cl in d.columns if grade_field_finding_regex.match(cl) ]
    return grade_fields[0]

def same_grade_different_subjects(d, columns):
    cross_class_comparison = {}

    grade_field = _get_grade_field(d)

    for i in range(len(d)):
        key = d['teacher'][i] + d['grade'][i]
        x = cross_class_comparison.get(key, {})
        x[d['subject'][i]] = d[grade_field][i]
        cross_class_comparison[key] = x

    print cross_class_comparison
    cross_class_comparison = DataFrame([ v for (k, v) in cross_class_comparison.iteritems() if len(v) == 2])

    print str(len(cross_class_comparison)) + " teachers who taught the same grade but different subjects"
    print "Correlation: " + str(corrcoef(cross_class_comparison.T))

    hexbin(cross_class_comparison[columns[0]], cross_class_comparison[columns[1]], gridsize=20)
    xlabel("English Language Arts")
    ylabel("Mathematics")
    colorbar()

def same_teacher_different_grade(d):
    cross_class_comparison = {}

    grade_field = _get_grade_field(d)

    for i in range(len(d)):
        key = d['teacher'][i] + d['subject'][i]
        x = cross_class_comparison.get(key, {})
        x[d['grade'][i]] = d[grade_field][i]
        cross_class_comparison[key] = x

    cross_class_comparison = DataFrame([ v.values() for (k, v) in cross_class_comparison.iteritems() if len(v) == 2])

    print str(len(cross_class_comparison)) + " teachers who taught multiple grades"
    print "Correlation: " + str(corrcoef(cross_class_comparison.T))
    hexbin(cross_class_comparison[0], cross_class_comparison[1], gridsize=7)
    xlabel("One Grade")
    ylabel("Other Grade")
    colorbar()


def same_teacher_grade_subject_different_years():
    merged = merge(d2008, d2009, on=['teacher', 'subject', 'grade'])
    print "Same teacher/grade/subject data points = " + str(len(merged))
    print "Correlation: " + str(corrcoef([ merged['va_pctl_0809'], merged['va_pctl_0910'] ]))

    hexbin(merged['va_pctl_0809'], merged['va_pctl_0910'], gridsize=20)
    xlabel("2008-2009")
    ylabel("2009-2010")
    colorbar()


# Uncomment this to make my first graph
## same_teacher_grade_subject_different_years()
## show()


# Uncomment this to make my second graph

## subplot(221)
## title("Same teacher, different subject 2009")
## same_grade_different_subjects(d2009, ('English Language Arts', 'Mathematics'))

## subplot(222)
## title("Same teacher, different subject 2008")
## same_grade_different_subjects(d2008, ('ELA', 'MATH'))


## subplot(223)
## title("Same teacher, different grade2009")
## same_teacher_different_grade(d2009)
## subplot(224)
## title("Same teacher, different grade2008")
## same_teacher_different_grade(d2008)

## show()
