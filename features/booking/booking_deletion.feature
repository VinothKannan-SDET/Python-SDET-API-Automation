Feature: Booking Deletion

  @regression
  Scenario: Delete an existing booking successfully

    Given I have valid booking details

    When I create a booking
    And I delete the created booking

    Then the booking should be deleted successfully
    And the deleted booking should no longer exist