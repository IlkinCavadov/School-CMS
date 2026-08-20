import { createContext, useContext, useState } from "react";

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
    const [token, setToken] = useState(
        () => localStorage.getItem("access_token")
    );

    function login(accessToken) {
        localStorage.setItem("access_token", accessToken);
        setToken(accessToken);
    }

    function logout() {
        localStorage.removeItem("access_token");
        setToken(null);
    }

    const isAuthenticated = Boolean(token);

    return (
        <AuthContext.Provider
            value={{
                token,
                isAuthenticated,
                login,
                logout,
            }}
        >
            {children}
        </AuthContext.Provider>
    );
}

export function useAuth() {
    return useContext(AuthContext);
}