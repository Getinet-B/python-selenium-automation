# Created by getinet at 4/30/2024
Feature: Test Open and Close Between Two Pages
  # This test opens login page clicks on Terms and Conditions
  # and return back to login page
  Scenario: User can open and close Terms and Conditions from sign in page
    # Enter steps here
    Given Open Target
    When click Sign In button
    And click Sign In button on side navigation menu
    Given Open sign in page
    When Store original window
    And Click on Target terms and conditions link
    And Switch to the newly opened window
    Then Verify Terms and Conditions page is opened
    And close current page
    And Return to original window
