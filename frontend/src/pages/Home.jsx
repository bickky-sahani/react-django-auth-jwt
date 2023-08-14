import React, { useState, useEffect } from "react";
import {
  Container,
  Grid,
  Paper,
  Typography,
  List,
  ListItem,
  ListItemText,
} from "@mui/material";
import axios from "axios";
import { toast, ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

export const Home = () => {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    const token = localStorage.getItem("tokens");
    const headers = { Authorization: `Bearer ${token}` };

    axios
      .get("http://localhost:8000/api/task/", { headers })
      .then((response) => {
        setTasks(response.data);
      })
      .catch((error) => {
        //console.error("Error fetching tasks:", error);
        toast.error(
          "Error fetching tasks: " + error.response.data.messages.message
        );
      });
  }, []);

  return (
    <Container maxWidth="sm">
      <Typography variant="h4" align="center" gutterBottom>
        Task List
      </Typography>
      <List>
        {tasks.map((task) => (
          <ListItem key={task.id} disablePadding>
            <ListItemText primary={task.title} secondary={task.description} />
          </ListItem>
        ))}
      </List>
    </Container>
  );
};
