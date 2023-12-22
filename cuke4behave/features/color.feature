Feature: Color selection

  Rule: User can select a profile color

    Scenario: User selects a valid color
      Given I am on the profile customization page
      When I select the color "red"
      Then the profile color should change to "red"
