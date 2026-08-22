import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { AuthProvider } from "./auth/AuthContext";
import DashboardLayout from "./layouts/DashboardLayout";
import Dashboard from "./pages/Dashboard";
import Login from "./pages/Login";
import Students from "./pages/Students";




function Employees() {
    return <h1>Employees</h1>;
}

function Teachers() {
    return <h1>Teachers</h1>;
}

function Users() {
    return <h1>Users</h1>;
}

function Classes() {
    return <h1>Classes</h1>;
}

function Subjects() {
    return <h1>Subjects</h1>;
}

function SubjectAssignments() {
    return <h1>Subject Assignments</h1>;
}

function Rooms() {
    return <h1>Rooms</h1>;
}

function Profile() {
    return <h1>Profile</h1>;
}

function App() {
    return (
      <AuthProvider>
        <BrowserRouter>
            <Routes>
              <Route path="/login" element={<Login />} />
                <Route element={<DashboardLayout />}>

                    <Route
                        path="/dashboard"
                        element={<Dashboard />}
                    />

                    <Route
                        path="/students"
                        element={<Students />}
                    />

                    <Route
                        path="/employees"
                        element={<Employees />}
                    />

                    <Route
                        path="/teachers"
                        element={<Teachers />}
                    />

                    <Route
                        path="/users"
                        element={<Users />}
                    />

                    <Route
                        path="/classes"
                        element={<Classes />}
                    />

                    <Route
                        path="/subjects"
                        element={<Subjects />}
                    />

                    <Route
                        path="/subject-assignments"
                        element={<SubjectAssignments />}
                    />

                    <Route
                        path="/rooms"
                        element={<Rooms />}
                    />

                    <Route
                        path="/profile"
                        element={<Profile />}
                    />

                </Route>

                <Route
                    path="*"
                    element={<Navigate to="/dashboard" replace />}
                />

            </Routes>
        </BrowserRouter>
      </AuthProvider>  
    );
}

export default App;