import {NavLink,  Outlet } from "react-router-dom";

function DashboardLayout() {
    const navigation = [
        {
            label: null,
            items: [
                { id: "dashboard", label: "Dashboard", href: "/dashboard" },
            ],
        },
        {
            label: "People",
            items: [
                { id: "students", label: "Students", href: "/students" },
                { id: "employees", label: "Employees", href: "/employees" },
                { id: "teachers", label: "Teachers", href: "/teachers" },
            ],
        },
        {
            label: "Academics",
            items: [
                { id: "classes", label: "Classes", href: "/classes" },
                { id: "subjects", label: "Subjects", href: "/subjects" },
                {
                    id: "subject-assignments",
                    label: "Subject Assignments",
                    href: "/subject-assignments",
                },
            ],
        },
        {
            label: "School",
            items: [
                { id: "rooms", label: "Rooms", href: "/rooms" },
            ],
        },
        {
            label: "Administration",
            items: [
                { id: "users", label: "Users", href: "/users" },
            ],
        },
    ];

    return (
        <div className="app-layout">

            <aside className="sidebar">

                <div className="sidebar-brand">
                    <div className="school-name">
                        Greenfield School
                    </div>

                    <div className="school-subtitle">
                        Management System
                    </div>
                </div>

                <nav className="sidebar-navigation">

                    {navigation.map((group) => (
                        <div
                            className="navigation-group"
                            key={group.label ?? "main"}
                        >

                            {group.label && (
                                <div className="navigation-label">
                                    {group.label}
                                </div>
                            )}

                            {group.items.map((item) => (
                                <NavLink
                                    key={item.id}
                                    to={item.href}
                                    className={({isActive})  => 
                                            `navigation-item ${isActive ? "active" : ""}`
                                                }
                                >
                                    {item.label}
                                </NavLink>
                            ))}

                        </div>
                    ))}

                </nav>

                <div className="sidebar-footer">
                    <NavLink
                        to="/profile"
                        className={({ isActive }) =>
                            `navigation-item ${isActive ? "active" : ""}`
                        }
                    >
                        Profile
                    </NavLink>

                    <a href="/login" className="navigation-item">
                        Logout
                    </a>
                </div>

            </aside>

            <div className="main-area">

                <header className="top-header">

                    <div className="user-information">
                        <div className="user-name">
                            Admin User
                        </div>

                        <div className="user-role">
                            SuperAdmin
                        </div>
                    </div>

                    <div className="user-avatar">
                        AD
                    </div>

                </header>

                <main className="page-content">
                    <Outlet />
                </main>

            </div>

        </div>
    );
}

export default DashboardLayout;