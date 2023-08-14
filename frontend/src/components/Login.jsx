import {
  Container,
  Grid,
  Paper,
  TextField,
  Button,
  InputAdornment,
  IconButton,
  Typography,
} from "@mui/material";
import VisibilityIcon from "@mui/icons-material/Visibility";
import VisibilityOffIcon from "@mui/icons-material/VisibilityOff";
import { React, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";

import { toast, ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

export const Login = () => {
  const navigate = useNavigate();

  const [values, setValues] = useState({
    email: "",
    pass: "",
    showPass: false,
  });
  const handleLogin = (e) => {
    e.preventDefault();

    axios
      .post("http://localhost:8000/api/user/login/", {
        email: values.email,
        password: values.pass,
      })
      .then((res) => {
        localStorage.setItem("tokens", res.data.tokens.access);
        toast.success("Login successful!");
        navigate("/home");
      })
      .catch((err) => {
        console.log(err);
        toast.error(err.response.data.error);
      });
  };

  const handlePassVisibilty = () => {
    setValues({
      ...values,
      showPass: !values.showPass,
    });
  };

  return (
    <div className="App">
      <ToastContainer />

      <Container maxWidth="sm">
        <Grid
          container
          spacing={2}
          direction={"column"}
          justifyContent={"center"}
          style={{ minHeight: "50vh" }}
        >
          <h2>Login</h2>

          <Paper elevation={2} sx={{ padding: 5 }}>
            <form onSubmit={handleLogin}>
              <Grid container direction={"column"} spacing={2}>
                <Grid item>
                  <TextField
                    type="email"
                    fullWidth
                    label="Enter your email"
                    placeholder="Email Address"
                    variant="outlined"
                    required
                    onChange={(e) =>
                      setValues({
                        ...values,
                        email: e.target.value,
                      })
                    }
                  />
                </Grid>
                <Grid item>
                  <TextField
                    type={values.showPass ? "text" : "password"}
                    fullWidth
                    label="Enter your password"
                    placeholder="Password"
                    variant="outlined"
                    required
                    onChange={(e) =>
                      setValues({
                        ...values,
                        pass: e.target.value,
                      })
                    }
                    InputProps={{
                      endAdornment: (
                        <InputAdornment position="end">
                          <IconButton
                            onClick={handlePassVisibilty}
                            aria-label="toggle password visibility"
                            edge="end"
                          >
                            {" "}
                            {values.showPass ? (
                              <VisibilityIcon />
                            ) : (
                              <VisibilityOffIcon />
                            )}
                          </IconButton>
                        </InputAdornment>
                      ),
                    }}
                  />
                </Grid>
                <Grid item>
                  <Button type="submit" variant="contained">
                    Login
                  </Button>
                </Grid>
                <Grid item>
                  <Typography variant="h6" gutterBottom>
                    Don't have an account ? Click here to{" "}
                    <Button
                      component={Link}
                      to="/register"
                      variant="contained"
                      color="success"
                    >
                      Register
                    </Button>
                  </Typography>
                </Grid>
              </Grid>
            </form>
          </Paper>
        </Grid>
      </Container>
    </div>
  );
};
