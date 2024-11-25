import React, { useState, useEffect } from "react";

function Homepage() {
  const [farmers, setFarmers] = useState([]);
  const [buyers, setBuyers] = useState([]);
  const [pendingFarmers, setPendingFarmers] = useState([]);

  // Fetch data from JSON files
  useEffect(() => {
    fetch("/farmers.json")
      .then((response) => response.json())
      .then((data) =>
        setFarmers(data.map((farmer) => ({ ...farmer, disabled: false })))
      );

    fetch("/buyers.json")
      .then((response) => response.json())
      .then((data) =>
        setBuyers(data.map((buyer) => ({ ...buyer, disabled: false })))
      );

    fetch("/pendingFarmers.json")
      .then((response) => response.json())
      .then((data) => setPendingFarmers(data));
  }, []);

  const deleteFarmer = (index) => {
    const updatedFarmers = [...farmers];
    updatedFarmers.splice(index, 1);
    setFarmers(updatedFarmers);
  };

  const deleteBuyer = (index) => {
    const updatedBuyers = [...buyers];
    updatedBuyers.splice(index, 1);
    setBuyers(updatedBuyers);
  };

  const approveFarmer = (index) => {
    const farmerToApprove = pendingFarmers[index];
    setFarmers([...farmers, { ...farmerToApprove, disabled: false }]);
    const updatedPendingFarmers = [...pendingFarmers];
    updatedPendingFarmers.splice(index, 1);
    setPendingFarmers(updatedPendingFarmers);
  };

  const disapproveFarmer = (index) => {
    const reason = window.prompt(
      "Please provide a reason for disapproval:",
      "Not specified"
    );
    if (reason) {
      const updatedPendingFarmers = [...pendingFarmers];
      updatedPendingFarmers.splice(index, 1);
      setPendingFarmers(updatedPendingFarmers);
      window.alert(`Disapproval reason: ${reason}`);
    }
  };

  const handleEdit = (index, type) => {
    const updatedData = type === "farmer" ? [...farmers] : [...buyers];
    const item = updatedData[index];
    const updatedItem = { ...item };

    Object.keys(item).forEach((key) => {
      if (key !== "disabled") {
        const newValue = prompt(`Edit ${key} (current: ${item[key]})`, item[key]);
        if (newValue !== null && newValue.trim() !== "") {
          updatedItem[key] = key === "phone" || key === "farm_size" ? +newValue : newValue;
        }
      }
    });

    updatedData[index] = updatedItem;
    type === "farmer" ? setFarmers(updatedData) : setBuyers(updatedData);
  };

  const toggleDisable = (index, type) => {
    if (type === "farmer") {
      const updatedFarmers = [...farmers];
      updatedFarmers[index].disabled = !updatedFarmers[index].disabled;
      setFarmers(updatedFarmers);
    } else if (type === "buyer") {
      const updatedBuyers = [...buyers];
      updatedBuyers[index].disabled = !updatedBuyers[index].disabled;
      setBuyers(updatedBuyers);
    }
  };

  const tableStyle = {
    width: "100%",
    marginBottom: "20px",
    textAlign: "center",
    borderCollapse: "collapse",
  };

  const tableHeaderStyle = {
    backgroundColor: "#d4edda",
    color: "#155724",
    fontWeight: "bold",
  };

  const buttonStyle = {
    marginRight: "10px",
    padding: "5px 10px",
    backgroundColor: "#28a745",
    color: "white",
    border: "none",
    borderRadius: "4px",
    cursor: "pointer",
  };

  const disabledButtonStyle = {
    ...buttonStyle,
    backgroundColor: "#6c757d",
    cursor: "not-allowed",
  };

  return (
    <div style={{ padding: "20px", backgroundColor: "#f8f9fa" }}>
      <h1 style={{ color: "#155724" }}>Admin's Dashboard</h1>

      {/* Farmers Table */}
      <h2>Farmers</h2>
      <table border="1" style={tableStyle}>
        <thead>
          <tr style={tableHeaderStyle}>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Email</th>
            <th>Phone</th>
            <th>Farm Size</th>
            <th>Farm Address</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {farmers.map((farmer, index) => (
            <tr key={index}>
              <td>{farmer.first_name}</td>
              <td>{farmer.last_name}</td>
              <td>{farmer.email}</td>
              <td>{farmer.phone}</td>
              <td>{farmer.farm_size}</td>
              <td>{farmer.farm_address}</td>
              <td>
                <button
                  style={buttonStyle}
                  onClick={() => handleEdit(index, "farmer")}
                >
                  Edit
                </button>
                <button
                  style={farmer.disabled ? disabledButtonStyle : buttonStyle}
                  onClick={() => toggleDisable(index, "farmer")}
                >
                  {farmer.disabled ? "Activate" : "Disable"}
                </button>
                <button style={buttonStyle} onClick={() => deleteFarmer(index)}>
                  Delete
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {/* Buyers Table */}
      <h2>Buyers</h2>
      <table border="1" style={tableStyle}>
        <thead>
          <tr style={tableHeaderStyle}>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Email</th>
            <th>Phone</th>
            <th>Delivery Address</th>
            <th>Preferred Payment</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {buyers.map((buyer, index) => (
            <tr key={index}>
              <td>{buyer.first_name}</td>
              <td>{buyer.last_name}</td>
              <td>{buyer.email}</td>
              <td>{buyer.phone}</td>
              <td>{buyer.delivery_address}</td>
              <td>{buyer.preferred_payment}</td>
              <td>
                <button
                  style={buttonStyle}
                  onClick={() => handleEdit(index, "buyer")}
                >
                  Edit
                </button>
                <button
                  style={buyer.disabled ? disabledButtonStyle : buttonStyle}
                  onClick={() => toggleDisable(index, "buyer")}
                >
                  {buyer.disabled ? "Activate" : "Disable"}
                </button>
                <button style={buttonStyle} onClick={() => deleteBuyer(index)}>
                  Delete
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {/* Pending Farmers Table */}
      <h2>Pending Farmers</h2>
      <table border="1" style={tableStyle}>
        <thead>
          <tr style={tableHeaderStyle}>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Email</th>
            <th>Phone</th>
            <th>Farm Size</th>
            <th>Farm Address</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {pendingFarmers.map((farmer, index) => (
            <tr key={index}>
              <td>{farmer.first_name}</td>
              <td>{farmer.last_name}</td>
              <td>{farmer.email}</td>
              <td>{farmer.phone}</td>
              <td>{farmer.farm_size}</td>
              <td>{farmer.farm_address}</td>
              <td>
                <button
                  style={buttonStyle}
                  onClick={() => approveFarmer(index)}
                >
                  Approve
                </button>
                <button
                  style={buttonStyle}
                  onClick={() => disapproveFarmer(index)}
                >
                  Disapprove
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Homepage;







