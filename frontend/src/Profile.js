import { useNavigate } from "react-router";

export default function Profile(){
    const navigate = useNavigate();

    const signOut = () => {
        localStorage.removeItem("login-token");
        navigate("/");
    };


    return (
        <>
            <div style={{ marginTop: 20, minHeight: 700 }}>
                <h1>profile page</h1>
                <p>Hello there, welcome to your profile page</p>

                <button onClick={signOut}>sign out </button>
            </div>
        </>
    );
}