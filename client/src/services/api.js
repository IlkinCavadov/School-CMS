const API_URL = import.meta.env.VITE_API_URL;

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