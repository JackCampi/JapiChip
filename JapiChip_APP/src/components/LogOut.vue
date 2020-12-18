<template>
    <section id="notification_log_out">
        <div id="section_login_prin">
            <div id="section_login_seg">
                <div class="conteiner">
                    <h1>Do you wanna log out?</h1>
                    <div>
                        <form action="/action_page.php">
                            <input class="sumit" type="submit" value="Yes" />
                            <input class="sumit" type="submit" value="Cancel" />
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<style>
    @font-face {
        font-family: "Lobster";
        src: url("../../static/fonts/Lobster-Regular.ttf");
    }

    @font-face {
        font-family: "Chivo";
        src: url("../../static/fonts/Chivo-Regular.ttf");
    }

    * {
        margin: 0;
        padding: 0;
        font-family: "Chivo";
    }

    #notification_log_out {
        width: 100%;
        height: 80vh;
        display: flex;
        align-items: center;
        background-color: white;
    }

    #section_login_prin {
        display: flex;
        justify-content: center;
        width: 100%;
        margin: 0 auto;
        position: relative;
    }

    #section_login_seg {
        display: flex;
        align-items: center;
        height: 20vh;
        width: 40%;
        text-align: center;
        border: 1px solid #666;
        box-shadow: 2px 2px 10px #666;
        background-color: #f5f3f3;
    }

    .conteiner {
        width: 100%;
        height: 15vh;
    }

    #section_login_seg h1 {
        margin-top: 20px;
        margin-bottom: 10px;
        font-size: 15px;
    }

    .sumit {
        margin-bottom: 10px;
        margin-right: 7px;
        padding: 3px;
        width: 30%;
        border: 1px solid black;
        background-color: #b2e4ee;
    }

    .sumit:hover {
        cursor: pointer;
        background-color: #25BEDB;
    }
</style>