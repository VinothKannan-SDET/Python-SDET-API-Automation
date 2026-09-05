Feature: Booking Update

  @regression
  Scenario: Update an existing booking successfully

    Given I have valid booking details
    And I have updated booking details

    When I create a booking
    And I update the created booking

    Then the booking should be updated successfully
    And the updated booking should match the updated details