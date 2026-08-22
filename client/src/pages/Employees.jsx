import { useEffect, useState } from "react";
import { getEmployees } from "../services/employees";
import { useAuth } from "../auth/AuthContext";
import ReactPaginateModule from "react-paginate";
const ReactPaginate = ReactPaginateModule.default;
function Employees() {
    const { token } = useAuth();

    const [employees, setEmployees] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    const [currentPage, setCurrentPage] = useState(0);
    const itemsPerPage = 5;

    const offset = currentPage * itemsPerPage;

    const paginatedItems = employees.slice(
        offset,
        offset + itemsPerPage
    );

    const handlePageChange = ({ selected }) => {
        setCurrentPage(selected);
    };

    useEffect(() => {
        async function loadEmployees() {
            try {
                setError("");

                const data = await getEmployees(token);

                setEmployees(data);
            } catch (error) {
                setError("Failed to load employees.");
            } finally {
                setLoading(false);
            }
        }

        loadEmployees();
    }, [token]);

    return (
        <div className="employees-page">
            <div className="page-header">
                <div>
                    <h1>Employees</h1>
                    <p>
                        Manage employees at Greenfield School.
                    </p>
                </div>

                <button className="primary-button">
                    Add Employee
                </button>
            </div>

            <section className="content-card">
                <div className="table-toolbar">
                    <div>
                        <h2>All Employees</h2>
                        <p>
                            Employees currently registered in the system.
                        </p>
                    </div>

                    <input
                        className="table-search"
                        type="search"
                        placeholder="Search employees..."
                    />
                </div>

                <div className="table-wrapper">
                    <table className="data-table">
                        <thead>
                            <tr>
                                <th>Name</th>
                                <th>Username</th>
                                <th>Email</th>
                                <th>Employee Type</th>
                                <th>Actions</th>
                            </tr>
                        </thead>

                        <tbody>
                            {loading && (
                                <tr>
                                    <td colSpan="5">
                                        Loading employees...
                                    </td>
                                </tr>
                            )}

                            {!loading && error && (
                                <tr>
                                    <td colSpan="5">
                                        {error}
                                    </td>
                                </tr>
                            )}

                            {!loading &&
                                !error &&
                                employees.length === 0 && (
                                    <tr>
                                        <td colSpan="5">
                                            No employees found.
                                        </td>
                                    </tr>
                                )}

                            {!loading &&
                                !error &&
                                paginatedItems.map((employee) => (
                                    <tr key={employee.id}>
                                        <td>
                                            <strong>
                                                {employee.first_name}{" "}
                                                {employee.last_name}
                                            </strong>
                                        </td>

                                        <td>
                                            {employee.username}
                                        </td>

                                        <td>
                                            {employee.email}
                                        </td>

                                        <td>
                                            <span className="status-badge status-active">
                                                {employee.employee_type}
                                            </span>
                                        </td>

                                        <td>
                                            <button className="table-action">
                                                View
                                            </button>

                                            <button className="table-action">
                                                Edit
                                            </button>
                                        </td>
                                    </tr>
                                ))}
                        </tbody>
                    </table>
                </div>

                {!loading && !error && employees.length > itemsPerPage && (
                    <ReactPaginate
                        previousLabel="‹"
                        nextLabel="›"
                        breakLabel="..."
                        breakClassName="pagination-break"
                        pageCount={Math.ceil(
                            employees.length / itemsPerPage
                        )}
                        marginPagesDisplayed={2}
                        pageRangeDisplayed={3}
                        onPageChange={handlePageChange}
                        containerClassName="pagination"
                        activeClassName="pagination-active"
                        pageLinkClassName="pagination-link"
                        previousLinkClassName="pagination-previous"
                        nextLinkClassName="pagination-next"
                        disabledClassName="pagination-disabled"
                    />
                )}
            </section>
        </div>
    );
}

export default Employees;