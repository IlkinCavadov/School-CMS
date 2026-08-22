import { useEffect, useState } from "react";
import { getStudents } from "../services/students";
import { useAuth } from "../auth/AuthContext";
import ReactPaginateModule from 'react-paginate';


const ReactPaginate = ReactPaginateModule.default;

console.log(ReactPaginate);

function Students() {
const { token } = useAuth();
const [currentPage, setCurrentPage] = useState(0);
const itemsPerPage = 5
const offset = currentPage * itemsPerPage

const [students, setStudents] = useState([]);
const [loading, setLoading] = useState(true);
const paginatedItems = students.slice(offset, offset + itemsPerPage)
const [error, setError] = useState("");

const handlePageChange = ({ selected }) => {
  setCurrentPage(selected);
};



useEffect(() => {
    async function loadStudents() {
        try {
            setError("");

            const data = await getStudents(token);

            setStudents(data);
        } catch (error) {
            setError("Failed to load students.");
        } finally {
            setLoading(false);
        }
    }

    loadStudents();
}, [token]);
    return (
        <div className="students-page">
            <div className="page-header">
                <div>
                    <h1>Students</h1>
                    <p>Manage students enrolled at Greenfield School.</p>
                </div>

                <button className="primary-button">
                    Add Student
                </button>
            </div>
    <section className="content-card">
    <div className="table-toolbar">
        <div>
            <h2>All Students</h2>
            <p>Students currently registered in the system.</p>
        </div>

        <input
            className="table-search"
            type="search"
            placeholder="Search students..."
        />
    </div>

    <div className="table-wrapper">
        <table className="data-table">
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Class</th>
                    <th>Status</th>
                    <th>Actions</th>
                </tr>
            </thead>

<tbody>
    {loading && (
        <tr>
            <td colSpan="5">Loading students...</td>
        </tr>
    )}

    {!loading && error && (
        <tr>
            <td colSpan="5">{error}</td>
        </tr>
    )}

    {!loading && !error && students.length === 0 && (
        <tr>
            <td colSpan="5">No students found.</td>
        </tr>
    )}

    {!loading &&
        !error &&
        paginatedItems.map((student) => (
            <tr key={student.id}>
                <td>
                    <strong>
                        {student.first_name} {student.last_name}
                    </strong>
                </td>

                <td>{student.email}</td>

                <td>—</td>

                <td>
                    <span className="status-badge status-active">
                        Active
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
        <ReactPaginate
        previousLabel="<"
        nextLabel=">"
        breakLabel={"..."}
        breakClassName="paginationBreak"
        pageCount={Math.ceil(students.length / itemsPerPage)}
        marginPagesDisplayed={5}
        pageRangeDisplayed={2}
        onPageChange={handlePageChange}
        containerClassName="pagination"
        activeClassName="pagination-active"
        pageLinkClassName="pagination-link"
        previousLinkClassName="pagination-previous"
        nextLinkClassName="pagination-next"
        disabledClassName="pagination-disabled"

      />
  
    
</section>

        </div>
        
    );
    
}

export default Students;