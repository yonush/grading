Feature: determine the grade from select results

  Scenario: determine the grade
     Given an instance of the grades
      When the results are [50,50,50]
      Then the grade will be C-

      