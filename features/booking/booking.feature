Feature: Booking API

  Scenario: Create a new booking successfully

    Given I have valid booking details
    When I create a booking
    Then the booking should be created successfully
    And the booking response should contain the expected details