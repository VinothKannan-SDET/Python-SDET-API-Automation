Feature: Booking Creation

  Background:
    Given I have valid booking details

  Scenario: Create a new booking successfully

    When I create a booking
    Then the booking should be created successfully
    And the booking response should contain the expected details


  Scenario Outline: Create bookings with different first names

    When I create a booking with first name "<firstname>"
    Then the booking should be created successfully
    And the booking first name should be "<firstname>"

    Examples:
      | firstname |
      | John      |
      | David     |
      | Michael   |