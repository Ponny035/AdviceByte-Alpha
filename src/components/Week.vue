<template>
    <!-- third col -->
    <div class="Week col-md-3">
        <!-- ranking card list -->
        <div class="card" style="width: 18rem;">
            <div class="border-custom-up">
                <p class="cardhd">Weekly Ranking</p>
            </div>
            <table class="table table-hover table-light">
                <tbody>
                    <tr>
                        <th scope="row" class="font-custom-list">1</th>
                        <td class>
                            <img
                                src="../image/1.jpg"
                                alt
                                class="rounded-circle"
                            />
                        </td>
                        <td class="font-custom-list">Kritchagamol</td>
                        <td class="font-custom-list">isus</td>
                    </tr>
                </tbody>
            </table>
            <div class="border-custom">
                <a href="#" class="seemore">See more</a>
            </div>
        </div>
        <div class="boxspace-card"></div>
        <!-- เว้นบรรทัด -->
        <div class="card" style="width: 18rem;">
            <div class="border-custom-up">
                <p class="cardhd">Daily Mission</p>
            </div>
            <table class="table table-hover table-light" style="width: 18rem;">
                <tbody class="d-flex bd-highlight">
                    <tr>
                        <th scope="row" class="type-mission">[Daily]</th>
                        <td
                            class="text-left font-custom-list p-2 flex-fill bd-highlight"
                        >
                            Example Mission With Something
                            <p class="mission-detail">fake detail</p>
                        </td>
                    </tr>
                </tbody>
            </table>
            <div class="border-custom">
                <a href="#" class="seemore">See more</a>
            </div>
        </div>
    </div>
</template>

<script>
export default {}
</script>

<style>
.type-mission {
    font-family: Poppins;
    color: #ffaa00;
    font-size: 12px;
    font-weight: bold;
}
</style>
