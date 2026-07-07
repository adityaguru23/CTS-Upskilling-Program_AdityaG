import React from "react";
import { render, screen, fireEvent } from "@testing-library/react";
import "@testing-library/jest-dom";
import axios from "axios";
import UserProfile from "../src/UserProfile";

jest.mock("axios");

describe("UserProfile Component Tests", () => {
  afterEach(() => {
    jest.clearAllMocks();
  });

  test("loads and displays user profile", async () => {
    axios.get.mockResolvedValue({
      data: {
        name: "Cypher King",
        role: "Cloud Engineer",
      },
    });

    render(<UserProfile userId="999" />);

    const button = screen.getByRole("button", {
      name: /Load Profile Info/i,
    });

    fireEvent.click(button);

    expect(await screen.findByTestId("profile-display")).toBeInTheDocument();

    expect(screen.getByText("Name: Cypher King")).toBeInTheDocument();
    expect(screen.getByText("Role: Cloud Engineer")).toBeInTheDocument();

    expect(axios.get).toHaveBeenCalledWith(
      "https://api.example.com/users/999"
    );
  });

  test("shows an error message when request fails", async () => {
    axios.get.mockRejectedValue(new Error("Request Failed"));

    render(<UserProfile userId="999" />);

    fireEvent.click(
      screen.getByRole("button", {
        name: /Load Profile Info/i,
      })
    );

    expect(
      await screen.findByText(/failed to fetch user data/i)
    ).toBeInTheDocument();
  });
});