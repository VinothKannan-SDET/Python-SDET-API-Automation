Feature: Booking Retrieval

  @smoke
  @regression
  @contract
  Scenario: Retrieve a newly created booking successfully

    Given I have valid booking details
    When I create a booking
    And I retrieve the created booking
    Then the booking should be retrieved successfully
    And the retrieved booking should match the booking details