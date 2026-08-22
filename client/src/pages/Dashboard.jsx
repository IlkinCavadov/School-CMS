import { Link } from "react-router-dom";

function Dashboard() {
    return (
        <div className="dashboard">
            <div className="page-header">
                <div>
                    <h1>Dashboard</h1>
                    <p>Overview of Greenfield School.</p>
                </div>
            </div>

            <div className="dashboard-stats">
                <div className="stat-card">
                    <span className="stat-label">Students</span>
                    <strong className="stat-value">—</strong>
                </div>

                <div className="stat-card">
                    <span className="stat-label">Employees</span>
                    <strong className="stat-value">—</strong>
                </div>

                <div className="stat-card">
                    <span className="stat-label">Teachers</span>
                    <strong className="stat-value">—</strong>
                </div>

                <div className="stat-card">
                    <span className="stat-label">Classes</span>
                    <strong className="stat-value">—</strong>
                </div>
            </div>
            <div className="dashboard-grid">
    <section className="dashboard-card">
        <div className="dashboard-card-header">
            <div>
                <h2>Recent Activity</h2>
                <p>Latest activity in the system.</p>
            </div>
        </div>

        <div className="activity-list">
            <div className="activity-item">
                <div>
                    <strong>New student registered</strong>
                    <span>Student management</span>
                </div>
                <time>Today</time>
            </div>

            <div className="activity-item">
                <div>
                    <strong>Employee profile updated</strong>
                    <span>Employee management</span>
                </div>
                <time>Yesterday</time>
            </div>

            <div className="activity-item">
                <div>
                    <strong>New class created</strong>
                    <span>Academic management</span>
                </div>
                <time>2 days ago</time>
            </div>
        </div>
    </section>

    <section className="dashboard-card">
        <div className="dashboard-card-header">
            <div>
                <h2>Quick Actions</h2>
                <p>Common administrative tasks.</p>
            </div>
        </div>

        <div className="quick-actions">
            <Link to="/students">Add Student</Link>
            <Link to="/employees">Add Employee</Link>
            <Link to="/classes">Create Class</Link>
            <Link to="/subjects">Manage Subjects</Link>
        </div>
    </section>
</div>
        </div>
    );
}

export default Dashboard;