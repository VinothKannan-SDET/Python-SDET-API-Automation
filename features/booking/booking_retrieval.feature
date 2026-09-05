Feature: Booking retrieval

  Background:
    Given the API client is initialized

  Scenario: Retrieve an existing booking by ID
    Given an existing booking ID is available
    When I retrieve the booking by ID
    Then the booking should be retrieved successfully

  Scenario: Retrieve a newly created booking using its dynamic ID
    When I create a booking with valid details
    And I retrieve the created booking
    Then the retrieved booking should match the created booking

  Scenario: Return not found for a non-existing booking
    When I retrieve a booking using an invalid booking ID
    Then the booking should not be found