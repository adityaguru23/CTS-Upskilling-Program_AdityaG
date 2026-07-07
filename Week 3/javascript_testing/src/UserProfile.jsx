import React, { useState } from "react";
import axios from "axios";

function UserProfile({ userId }) {
  const [user, setUser] = useState(null);
  const [message, setMessage] = useState("");

  const getUser = async () => {
    try {
      const res = await axios.get(`https://api.example.com/users/${userId}`);
      setUser(res.data);
      setMessage("");
    } catch {
      setMessage("Unable to load profile");
    }
  };

  return (
    <div className="profile-card">
      <h2>User Details</h2>

      <button onClick={getUser}>Fetch User</button>

      {message && <p>{message}</p>}

      {user && (
        <div>
          <p>Name: {user.name}</p>
          <p>Role: {user.role}</p>
        </div>
      )}
    </div>
  );
}

export default UserProfile;