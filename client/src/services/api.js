const API_URL = "/api";

export async function getStudents(token) {
    const response = await fetch(`${API_URL}/students`, {
        headers: {
            Authorization: `Bearer ${token}`,
        },
    });

    if (!response.ok) {
        throw new Error("Failed to fetch students");
    }

    return response.json();
}