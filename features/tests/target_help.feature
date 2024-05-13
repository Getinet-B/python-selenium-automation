# Created by getinet at 5/8/2024
Feature: Tests for Target Help pages
  # Enter feature description here

  Scenario: User can select Help topic Promotions & Coupons
    Given Open Help page for Print a receipt
    Then Verify help  page Print a receipt opened
    When Select Help topic Delivery & Pickup
    Then Verify help Drive Up & Order Pickup page opened

  Scenario: User can select Help topic Target Account
    Given Open Help page for Print a receipt
    Then Verify help  page Print a receipt opened
    When Select help topic Target Account
    Then Verify help Create account page opened