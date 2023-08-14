import React from "react";
import { Navigate } from "react-router-dom";
import { Home } from "../pages/Home";
export const Protected = () => {
  const tokens = localStorage.getItem("tokens");

  if (!tokens) {
    return <Navigate to="/" replace />;
  }
  return <Home />;
};
